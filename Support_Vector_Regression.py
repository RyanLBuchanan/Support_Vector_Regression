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


# Feature Scaling


# Train the SVR model on the whole dataset


# Predict a new result


# Visualize the SVR results


# Visualize the SVR results (for higher resolution and smooth curve)


