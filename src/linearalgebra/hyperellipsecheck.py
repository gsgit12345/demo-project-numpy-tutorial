import numpy as np


def checkHypereclispe(point,axes):

    """
    point : list or array [x1, x2, ..., xn]
    axes  : list or array [a1, a2, ..., an]
    """
    point_array=np.array(point,dtype=float)
    axes_array=np.array(axes,dtype=float)

    value=np.sum(point_array**2) /(axes_array**2)

    if value < 1:
        return "Inside"
    elif value == 1:
        return "On boundary"
    else:
        return "Outside"


# Example 2D ellipse (a=3, b=2)
print(checkHypereclispe([1, 1], [3, 2]))

# Example 3D ellipsoid (a=3, b=2, c=4)
print(checkHypereclispe([1, 1, 1], [3, 2, 4]))