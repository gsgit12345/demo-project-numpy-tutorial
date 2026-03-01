# Line equation using normal vector:

# w · x + b = 0

# This is widely used in ML.


import numpy as np

def line_dot_product(x, w, b):
    """
    Computes w · x + b
    """
    x = np.array(x)
    w = np.array(w)
    
    return np.dot(w, x) + b


# Example
w = [2, -1]
b = -3
x = [1, 2]

result = line_dot_product(x, w, b)
print("w·x + b =", result)


# If result = 0 → point lies on line
# If > 0 → one side
# If < 0 → other side

# This is exactly how:

# Linear regression

# Logistic regression

# SVM

# Neural networks

# represent decision boundaries.