import numpy as np

# y = m x + b

def lineinterceptform(x,m,b):
    """
    Computes y = m*x + b
    """

    return m*x+b



x_values = np.linspace(-5, 5, 10)

y_values = lineinterceptform(x_values, m=2, b=1)

print("x:", x_values)
print("y:", y_values)

#This generates points on the line.