import numpy as np

def train_model(X, y):
    # Add bias column (1s)
    X = np.c_[np.ones(X.shape[0]), X]

    # Normal equation: theta = (X^T X)^-1 X^T y
    theta = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)
    return theta

def predict(theta, input_data):
    # Add bias term
    input_data = np.insert(input_data, 0, 1)
    return np.dot(input_data, theta)
