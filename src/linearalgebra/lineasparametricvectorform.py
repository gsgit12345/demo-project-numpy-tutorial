import numpy as np

# Line formula:

# r(t) = P0 + t d

# Where:

# P0 = starting point

# d = direction vector

def line_parametric(P0, d, t_values):
    """
    Computes parametric line points.
    """
    P0 = np.array(P0, dtype=float)
    d = np.array(d, dtype=float)
    
    return P0 + np.outer(t_values, d)


# Example
P0 = [1, 2]
d = [3, 4]
t = np.linspace(-2, 2, 5)

points = line_parametric(P0, d, t)

print("Points on line:\n", points)


# This gives multiple (x,y) points on the line.