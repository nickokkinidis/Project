Hello,

This is a small program in Python that performs multiple linear regression on a data set and uses the backward elimination process to determine the relevant variables.

# Brief Description of Backward Elimination
Backward elimination is a stepwise regression technique used to select the most significant variables in a multiple linear regression model. The process begins with all candidate variables included in the model. The variable with the highest p-value (least significant) is then removed, provided its p-value exceeds a pre-determined significance level (e.g., 0.05). This step is repeated iteratively: the model is re-fitted, and the next least significant variable is removed. The process continues until all remaining variables in the model have p-values below the significance threshold. This method helps in refining the model by excluding variables that do not contribute significantly to the predictive power, resulting in a simpler and more interpretable model.

# What does this program exactly do?

    1. Opens the data set.
    2. Converts categorical variables to numerical.
    3. Prompts the user for the target variable and the desired significance level.
    4. Runs the multiple linear regression with all the variables (excluding the target variable) and finds their p-values.
    5. Removes the variable with the highest p-value if it is above the significance level.
    6. Checks to see if the adjusted R squared is reduced.
    7. Repeats until only the relevant variables remain in the model and adjusted R squared is not reduced.

# Libraries:

    1. matplotlib.pyplot
    2. numpy
    3. pandas
    4. statsmodels.formula.api
