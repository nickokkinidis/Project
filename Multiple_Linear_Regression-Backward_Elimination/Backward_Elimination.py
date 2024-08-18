import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

"""
Note: Remove spaces and special characters from the column names.
TODO: make cat not hardcoded
add corected r2
"""

def main():
    # Read the target data set
    df = pd.read_csv('Dataset.csv')

    df_num = convert_categorical_to_numeric(df)

    print(df_num)
    

    #print(df)
   # model = backward_elimination(df)



def convert_categorical_to_numeric(df):
    # Get the categorical columns
    categorical_columns = []
    for col in df.columns:
        if pd.api.types.is_categorical_dtype(df[col]) or df[col].dtype == 'object':
            categorical_columns.append(col)

    # Initialize the merged DataFrame with the original DataFrame
    merged = df.copy()

    # Generate dummies for each categorical column and concatenate them to the original DataFrame
    for col in categorical_columns:
        dummies = pd.get_dummies(df[col], prefix=col)
        merged = pd.concat([merged, dummies], axis='columns')

    # Drop the original categorical columns
    merged = merged.drop(categorical_columns, axis='columns')

    return merged



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

    while len(cols) > 0:
        # create linear regression table using the columns from cols
        formula = f"{target_variable} ~ " + ' + '.join(cols)
        print(formula) # TODO: make style more nice
        model = smf.ols(formula=formula, data=df).fit()
    
        # find which column has the highest p-value
        p_values = model.p_values.drop('Intercept')  # excluding the intercept
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
    
    # print the final model
    formula_final = f"{target_variable} ~ " + ' + '.join(cols)
    model_final = smf.ols(formula=formula_final, data=df).fit()
    print(model_final.summary())
    print("The remaining columns are:", cols)

    return model_final


if __name__ == '__main__':
    main()
