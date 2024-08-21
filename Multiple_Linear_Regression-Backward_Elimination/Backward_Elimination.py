import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import re
import statsmodels.formula.api as smf

"""
TODO: inlcude the adjusted R squared check.
"""

def main():

    # read the target data set
    df = pd.read_csv('Dataset.csv')

    # convert categorical columns to numeric
    df_num = convert_categorical_to_numeric(df)

    # clean column names
    df_clean = clean_column_names(df_num)

    # run backward elimination
    model = backward_elimination(df_clean)

    # print the final model
    print(model.summary())

def convert_categorical_to_numeric(df):
    # get the categorical columns
    categorical_columns = []
    for col in df.columns:
        if pd.api.types.is_categorical_dtype(df[col]) or df[col].dtype == 'object':
            categorical_columns.append(col)

    # initialize the merged DataFrame with the original DataFrame
    merged = df.copy()

    # generate dummies for each categorical column and concatenate them to the original DataFrame
    for col in categorical_columns:

        dummies = pd.get_dummies(df[col], prefix=col)
        dummies = dummies.iloc[:, :-1]  # Drop the last dummy column
        dummies = dummies.astype(int)   # Convert True/False to 1/0
        merged = pd.concat([merged, dummies], axis='columns')
    
    # drop the original categorical columns.
    merged = merged.drop(categorical_columns, axis='columns')

    return merged


def clean_column_names(df):
    
    df.columns = df.columns.str.replace(r'\s+', '_', regex=True)  # Replace spaces with underscores
    df.columns = df.columns.str.replace(r'[^\w]', '', regex=True)  # Remove special characters
    return df


def backward_elimination(df):

    # get the target variable
    target_variable = input("Enter the name of the target variable: ")
    if target_variable not in df.columns:
        print(f"Target variable '{target_variable}' not found in the dataframe columns.")
        return

    # read the significance level
    try:
        significance_level = float(input("Enter the significance level: "))
    except ValueError:
        print("Please enter a valid number for the significance level.")
        return
    
    # read the column names and exclude the target variable
    cols = list(df.columns)
    cols.remove(target_variable)

    # create adjusted R squared
    adjusted_r_squared = 0.0

    while len(cols) > 0:
        # create linear regression table using the columns from cols
        formula = f"{target_variable} ~ " + ' + '.join(cols)
        print(formula)
        model = smf.ols(formula=formula, data=df).fit()
    
        # find new adjusted R squared
        new_adjusted_r_squared = model.rsquared_adj

        # check if the new adjusted R squared is greater than the previous
        if new_adjusted_r_squared > adjusted_r_squared:
            adjusted_r_squared = new_adjusted_r_squared
        else:
            break

        # find which column has the highest p-value
        p_values = model.pvalues.drop('Intercept')  # excluding the intercept
        pmax = max(p_values)
        
        feature_with_pmax = p_values.idxmax()
        if pmax > significance_level:
            # remove that column
            cols.remove(feature_with_pmax)
        else:
            break
        
    if len(cols) == 0:
        print("No significant features were found.")
        return
    
    # create the final model
    formula_final = f"{target_variable} ~ " + ' + '.join(cols)
    model_final = smf.ols(formula=formula_final, data=df).fit()
    print("\nThe remaining values are:", cols)

    return model_final


if __name__ == '__main__':
    main()
