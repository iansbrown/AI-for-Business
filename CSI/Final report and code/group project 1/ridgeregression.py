# -*- coding: utf-8 -*-
"""RidgeRegression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14D7RIRkSWJQod2uTgl4u8x6JgvhdfCHG
"""

import numpy as np

class RidgeRegression:
    def __init__(self, alpha=1.0):
        self.alpha = alpha
        self.weights = None
        
    def fit(self, X, y):
        n_samples, n_features = X.shape
        X_T = X.T
        I = np.eye(n_features)
        self.weights = np.linalg.inv(X_T.dot(X) + self.alpha * I).dot(X_T).dot(y)
        
    def predict(self, X):
        return X.dot(self.weights)

X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])
y = np.array([1, 2, 3, 4, 5])

regressor = RidgeRegression(alpha=1.0)
regressor.fit(X, y)

test_X = np.array([[6, 7]])
test_y_pred = regressor.predict(test_X)

print(test_y_pred) # output: [6.28571429]