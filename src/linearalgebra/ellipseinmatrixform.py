import numpy as np

def ellipseinMatrixForm(point,a,b):

# Defines a function.

# point → (x₁, x₂)

# a → horizontal radius

# b → vertical radius

    x=np.array(point,dtype=float)

    A= np.array([[1/(a*a), 0],
              [0, 1/(b*b)]])
    value = x.T @ A @ x

    if value < 1:
        return "Inside ellipse"
    elif value == 1:
        return "On boundary"
    else:
        return "Outside ellipse"


print(ellipseinMatrixForm([1, 1], 3, 2))