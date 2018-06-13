import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import Imputer, LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
import statsmodels.formula.api as sm

# SETUP DATASET FROM .csv
dataset = pd.read_csv('50_Startups.csv')
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values

# ENCODE TEXT DEPENDENT VARIABLE
label_encoder_x = LabelEncoder()
x[:, 3] = label_encoder_x.fit_transform(x[:, 3])
one_hot_encoder = OneHotEncoder(categorical_features = [3])
x = one_hot_encoder.fit_transform(x).toarray()

# REMOVE ONE COLUMN OF ENCODED DUMMY DEPENDENT VARIABLE - AVOID TRAP
x = x[:, 1:]

# BUILD TRAINING (80%) AND TEST SETS (20%) - random_state to spit same results
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

# LINEAR REGRESSION
regressor = LinearRegression()
regressor.fit(x_train, y_train)

# LINEAR PREDICTION
y_pred = regressor.predict(x_test)

# statsmodels DOES NOT HANDLE b0 AUTOMATICALLY, ADD INTERCEPT COLUMN OF x0 = 1
x = np.append(arr = np.ones((50, 1)).astype(int), values = x, axis = 1) 

# CREATE WHAT SHOULD BE THE OPTIMAL MATRIX OF VARIABLES FOR PREDICTION OF Y
x_optimal = x[:, [0, 1, 2, 3, 4, 5]]

# CREATE NEW REGRESSOR FROM statsmodels LIBRARY Ordinary Least Squares
regressor_ols = sm.OLS(endog = y, exog = x_optimal).fit()

# CALL STATISTICAL SUMMARY FUNCTION
regressor_ols.summary()

# HIGHEST IS x2 (P = 0.99), REMOVE AND TRY AGAIN
x_optimal = x[:, [0, 1, 3, 4, 5]]
regressor_ols = sm.OLS(endog = y, exog = x_optimal).fit()
regressor_ols.summary()

# HIGHEST IS x1 (P = 0.94), REMOVE AND TRY AGAIN
x_optimal = x[:, [0, 3, 4, 5]]
regressor_ols = sm.OLS(endog = y, exog = x_optimal).fit()
regressor_ols.summary()

# HIGHEST IS x2 (P = 0.60), REMOVE AND TRY AGAIN
x_optimal = x[:, [0, 3, 5]]
regressor_ols = sm.OLS(endog = y, exog = x_optimal).fit()
regressor_ols.summary()

# HIGHEST IS x2 (P = 0.06), DECIDE IF REMOVE AND TRY AGAIN
x_optimal = x[:, [0, 3]]
regressor_ols = sm.OLS(endog = y, exog = x_optimal).fit()
regressor_ols.summary()



'''
 ---- AUTOMATIC BACKWARD ELIMINATION ----
 Backward Elimination with p-values only:

        import statsmodels.formula.api as sm
        def backwardElimination(x, sl):
            numVars = len(x[0])
            for i in range(0, numVars):
                regressor_OLS = sm.OLS(y, x).fit()
                maxVar = max(regressor_OLS.pvalues).astype(float)
                if maxVar > sl:
                    for j in range(0, numVars - i):
                        if (regressor_OLS.pvalues[j].astype(float) == maxVar):
                            x = np.delete(x, j, 1)
            regressor_OLS.summary()
            return x
         
        SL = 0.05
        X_opt = X[:, [0, 1, 2, 3, 4, 5]]
        X_Modeled = backwardElimination(X_opt, SL)

Backward Elimination with p-values and Adjusted R Squared:

        import statsmodels.formula.api as sm
        def backwardElimination(x, SL):
            numVars = len(x[0])
            temp = np.zeros((50,6)).astype(int)
            for i in range(0, numVars):
                regressor_OLS = sm.OLS(y, x).fit()
                maxVar = max(regressor_OLS.pvalues).astype(float)
                adjR_before = regressor_OLS.rsquared_adj.astype(float)
                if maxVar > SL:
                    for j in range(0, numVars - i):
                        if (regressor_OLS.pvalues[j].astype(float) == maxVar):
                            temp[:,j] = x[:, j]
                            x = np.delete(x, j, 1)
                            tmp_regressor = sm.OLS(y, x).fit()
                            adjR_after = tmp_regressor.rsquared_adj.astype(float)
                            if (adjR_before >= adjR_after):
                                x_rollback = np.hstack((x, temp[:,[0,j]]))
                                x_rollback = np.delete(x_rollback, j, 1)
                                print (regressor_OLS.summary())
                                return x_rollback
                            else:
                                continue
            regressor_OLS.summary()
            return x
         
        SL = 0.05
        X_opt = X[:, [0, 1, 2, 3, 4, 5]]
        X_Modeled = backwardElimination(X_opt, SL)
 
'''

