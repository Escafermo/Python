import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeClassifier

# SETUP DATASET FROM .csv (TEXT ALREADY ENCODED)
dataset = pd.read_csv('Social_Network_Ads.csv')
x = dataset.iloc[:, [2, 3]].values # x IS A MATRIX
y = dataset.iloc[:, 4].values # y IS A VECTOR


# BUILD TRAINING (75%) AND TEST SETS (25%) - random_state to spit same results
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state = 0)
 
# SCALE NUMERIC VARIABLES (NOT REALLY NECESSARY IN THIS CASE, WE USE ONLY TO PLOT GRAPHS WITH HIGH RES)
scaler_x = StandardScaler()
x_train = scaler_x.fit_transform(x_train) # FIT  = UNDERSTAND DATA (min, max, mean, stdev)
x_test = scaler_x.transform(x_test) # ONLY TRANSFORM, SINCE ALREADY UNDERSTOOD DATA FROM x_train FIT

# FIT CLASSIFIER TO MODEL
classifier = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
classifier.fit(x_train, y_train)

# PREDICT A NEW RESULT
y_pred = classifier.predict(x_test)

# MAKING CONFUSION MATRIX 
cm = confusion_matrix(y_test, y_pred)


# Visualising the Training set results
from matplotlib.colors import ListedColormap
X_set, y_set = x_train, y_train
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                c = ListedColormap(('red', 'green'))(i), label = j)
plt.title('Decision Tree Classifier (Training set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()

# Visualising the Test set results
from matplotlib.colors import ListedColormap
X_set, y_set = x_test, y_test
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                c = ListedColormap(('red', 'green'))(i), label = j)
plt.title('Decision Tree Classifier (Test set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
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

# REMOVE ONE COLUMN OF ENCODED DUMMY DEPENDENT VARIABLE - AVOID TRAP
x = x[:, 1:]

# ENCODE TEXT INDEPENDENT VARIABLE
label_encoder_y = LabelEncoder()
y = label_encoder_y.fit_transform(y)

# SCALE NUMERIC VARIABLES
scaler_x = StandardScaler()
scaler_y = StandardScaler()
x = scaler_x.fit_transform(x) 
y = scaler_y.fit_transform(y) 
# OR
scaler_x = StandardScaler()
x_train = scaler_x.fit_transform(x_train) # FIT  = UNDERSTAND DATA (min, max, mean, stdev)
x_test = scaler_x.transform(x_test) # ONLY TRANSFORM, SINCE ALREADY UNDERSTOOD DATA FROM x_train FIT
 ---- END ----
'''