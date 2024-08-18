Hello,

This is a small program in Python that performs multiple linear regression on a data set and uses the backward elimination process to determine the relevant variables.

# Brief Description of Backward Elimination
Backward elimination is a stepwise regression technique used to select the most significant variables in a multiple linear regression model. The process begins with all candidate variables included in the model. The variable with the highest p-value (least significant) is then removed, provided its p-value exceeds a pre-determined significance level (e.g., 0.05). This step is repeated iteratively: the model is re-fitted, and the next least significant variable is removed. The process continues until all remaining variables in the model have p-values below the significance threshold. This method helps in refining the model by excluding variables that do not contribute significantly to the predictive power, resulting in a simpler and more interpretable model.

# What does this program exactly do?

    1. Defines the `backward_elimination` function that takes a DataFrame as a parameter.
    Note: Remove spaces and special characters from the column names in the data set, at the moment it can't handle them.
    2. Prompts the user for the target variable and the desired significance level.
    3. Runs the multiple linear regression with all the variables (excluding the target variable) and finds their p-values.
    4. Removes the variable with the highest p-value if it is above the significance level.
    5. Repeats steps 3 and 4 until only the relevant variables remain in the model.

# Libraries:

    1. matplotlib.pyplot
    2. numpy
    3. pandas
    4. statsmodels.formula.api

# Example Usage:

    #Read the data set
    df = pd.read_csv('Dataset.csv')
    #Convert categorical variables to numeric, this will be included in the code at some point
    df['State'] = df['State'].astype('category').cat.codes
    #Call the backward_elimination function
    model = backward_elimination(df)
