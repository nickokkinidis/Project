"""
Here I'll list 5 linear regression models in Python. The models are:

1. All-in (when you know that all the variables are relevant)
2. Backward elimination
3. Forward selection
4. Bidirectional elimination
5. Score comparison

2-4 are also known as Stepwise Regression

"""

# Imports
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.formula.api as smf

# 1. All-in
def all_in(X, y):



# 2. Backward elimination (argument: dataframe, returns final model)
def backward_elimination(df):

    # read the target variable
    target_variable = input("Enter the name of the target variable: ")
    if target_variable not in df.columns:
        print(f"Target variable '{target_variable}' not found in the dataframe columns.")
        return

    # read the significance level
    try:
        sl = float(input("Enter the significance level: "))
    except ValueError:
        print("Please enter a valid number for the significance level.")
        return
    
    # read the column names and exclude the target variable
    cols = list(df.columns)
    cols.remove(target_variable)

    while len(cols) > 0:
        # create linear regression table using the columns from cols
        formula = f"{target_variable} ~ " + ' + '.join(cols)
        model = smf.ols(formula=formula, data=df).fit()

        # find which column has the highest p-value
        pvalues = model.pvalues.drop('Intercept')  # excluding the intercept
        pmax = max(pvalues)
        feature_with_pmax = pvalues.idxmax()
        if pmax > sl:
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