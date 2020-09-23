# Support Vector Regression tutorial from Machine Learning A-Z - SuperDataScience
# Input by Ryan L Buchanan 18SEP20

# Import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Import Dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values

print(X)

print(y)

# Reshape dependent variable into 2D column vector
y = y.reshape(len(y), 1)

# Display salaries vertically
print(y)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_y = StandardScaler()
X = sc_X.fit_transform(X)
y = sc_y.fit_transform(y)

print(X)

print(y)

# Train the SVR model on the whole dataset
from sklearn.svm import SVR
regressor = SVR(kernel = 'rbf')
 

# Predict a new result


# Visualize the SVR results


# Visualize the SVR results (for higher resolution and smooth curve)


