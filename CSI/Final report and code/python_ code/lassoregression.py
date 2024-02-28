# -*- coding: utf-8 -*-
"""LassoRegression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KUSQYPcNjKOq_JtNWizi1rA-5vAX5vlt
"""

import numpy as np

class LassoRegression:
    def __init__(self, alpha=1.0, max_iter=1000, tol=0.0001):
        self.alpha = alpha
        self.max_iter = max_iter
        self.tol = tol
        self.weights = None
        
    def soft_threshold(self, x, gamma):
        if x > 0 and gamma < abs(x):
            return x - gamma
        elif x < 0 and gamma < abs(x):
            return x + gamma
        else:
            return 0
        
    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        X_T = X.T
        for i in range(self.max_iter):
            for j in range(n_features):
                y_pred = X.dot(self.weights)
                rho = X_T[j, :].dot(y - y_pred + self.weights[j] * X[:, j])
                z = X_T[j, :].dot(X[:, j])
                self.weights[j] = self.soft_threshold(rho / z, self.alpha / z)
            if np.linalg.norm(y - X.dot(self.weights)) < self.tol:
                break
                
    def predict(self, X):
        return X.dot(self.weights)

X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])
y = np.array([1, 2, 3, 4, 5])

regressor = LassoRegression(alpha=1.0, max_iter=1000, tol=0.0001)
regressor.fit(X, y)

test_X = np.array([[6, 7]])
test_y_pred = regressor.predict(test_X)

print(test_y_pred) # output: [5.82215743]