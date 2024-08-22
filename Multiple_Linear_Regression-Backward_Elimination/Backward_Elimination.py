import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import re
import statsmodels.formula.api as smf

def main():

    # read the target data set
    df = pd.read_csv('Dataset.csv')

    # get the target variable and the desired significance level
    target_variable, significance_level = get_target_variable_and_significance_level(df)

    # convert categorical columns to numeric
    df_num = convert_categorical_to_numeric(df)

    # clean column names
    df_clean = clean_column_names(df_num)

    # run backward elimination
    model, cols = backward_elimination(df_clean, target_variable, significance_level)

    # print the final model
    print(model.summary())

    # plot the final model
    plot_model(df_clean, model, cols, target_variable)


def get_target_variable_and_significance_level(df):
    # print the column names with index numbers
    for i, col in enumerate(df.columns):
        print(f"{i}. {col}")

    # Get the target variable
    while True:
        variable_index = input("Choose the number of the target variable: ")
        try:
            variable_index = int(variable_index)
            if variable_index < 0 or variable_index >= len(df.columns):
                print("Index out of range. Please choose a valid number.")
                continue
            target_variable = df.columns[variable_index]
            break  # Exit the loop if valid input is received
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Clean the variable name
    target_variable = re.sub(r'\s+', '_', target_variable)  # Replace spaces with underscores
    target_variable = re.sub(r'[^\w]', '', target_variable)  # Remove non-alphanumeric characters

    # Get the significance level
    while True:
        significance_level = input("Enter the significance level (e.g., 0.05): ")
        try:
            significance_level = float(significance_level)
            if not (0 < significance_level < 1):
                print("Significance level must be between 0 and 1. Please enter a valid number.")
                continue
            break  # Exit the loop if valid input is received
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    
    return target_variable, significance_level
    

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


def backward_elimination(df, target_variable, significance_level):
    
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

    return model_final, cols


def plot_model(df, model, cols, target_variable):
    # create scatter plot
    for col in cols:
        # create scatter plot
        plt.scatter(df[col], df[target_variable], label='Data Points')
        plt.xlabel(col)
        plt.ylabel(target_variable)
        plt.title(f"{target_variable} vs. {col}")

        # Calculate the range of x values
        max_x = df[col].max()
        min_x = df[col].min()

        # Add the line of best fit
        mean_value = df[col].mean()
        all_else = sum(model.params[variable] * mean_value for variable in cols if variable != col)

        # Ensure to use the constant term properly
        intercept = model.params['const'] if 'const' in model.params else model.params['Intercept']
        slope = model.params[col]

        x = [min_x, max_x]
        y = intercept + np.array(x) * slope + all_else
        plt.plot(x, y, color='red', label='Fitted Line')
        
        # Create equation text with conditional logic
        intercept_text = f"{intercept:.2f}"
        slope_text = f"{slope:.2f}"
        other_vars_text = " + ".join([f"{model.params[var]:.2f} * {var}" for var in cols if var != col])

        equation_text = (
            f"y = {intercept_text}"
            f"{' + ' + slope_text + ' * ' + col if slope != 0 else ''}"
            f"{' + ' + other_vars_text if other_vars_text else ''}"
        ).strip(" + ")  # Remove any trailing ' + ' if it's at the end

        plt.text(min_x, y[-1], equation_text, color='red')

        # show plot
        plt.show()

if __name__ == '__main__':
    main()
