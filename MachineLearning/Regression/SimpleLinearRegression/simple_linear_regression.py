import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import Imputer, LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression

# SETUP DATASET FROM .csv
dataset = pd.read_csv('Salary_Data.csv')
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

# BUILD TRAINING (66%) AND TEST SETS (33%) - random_state to spit same results
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 1/3, random_state = 0)

# FIT SIMPLE LINEAR REGRESSION TO TRAINING SET
regressor = LinearRegression()
regressor.fit(x_train, y_train)

# PREDICT y USING FITTED REGRESSOR AND x_test CLEAN DATA
y_pred_test = regressor.predict(x_test)
y_pred_train = regressor.predict(x_train)


# VISUALIZE THE TRAINING SET RESULTS
plt.scatter(x_train, y_train, color='blue')
plt.plot(x_train, y_pred_train, color='red')
plt.title('(Train) Salary x Time')
plt.xlabel('Years')
plt.ylabel('Salary')
plt.show()


# VISUALIZE THE TEST SET RESULTS
plt.scatter(x_test, y_test, color='green')
plt.plot(x_train, y_pred_train, color='red')
plt.title('(Test) Salary x Time')
plt.xlabel('Years')
plt.ylabel('Salary')
plt.show()







'''
 ---- OPTIONAL----
 
# IMPUTE MISSING VALUES (NaN) AS MEAN
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(x[:, 1:3])
x[:, 1:3] = imputer.transform(x[:, 1:3])

# ENCODE TEXT DEPENDENT VARIABLE
label_encoder_x = LabelEncoder()
x[:,0] = label_encoder_x.fit_transform(x[:,0])
one_hot_encoder = OneHotEncoder(categorical_features = [0])
x = one_hot_encoder.fit_transform(x).toarray()

# ENCODE TEXT INDEPENDENT VARIABLE
label_encoder_y = LabelEncoder()
y = label_encoder_y.fit_transform(y)

# SCALE NUMERIC DEPENDENT VARIABLES FROM -> EVEN THE DUMMY VARIABLES 0 and 1 FOR COUNTRY
scaler_x = StandardScaler()
x_train = scaler_x.fit_transform(x_train) # FIT  = UNDERSTAND DATA (min, max, mean, stdev)
x_test = scaler_x.transform(x_test) # ONLY TRANSFORM, SINCE ALREADY UNDERSTOOD DATA FROM x_train FIT
 ---- END ----
'''