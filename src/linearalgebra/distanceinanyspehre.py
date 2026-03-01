def hypersphere_check(point, radius):

    distance_squared = 0

    # Add square of each coordinate
    for value in point:
        distance_squared += value * value

    if distance_squared < radius * radius:
        return "Inside"
    elif distance_squared == radius * radius:
        return "On boundary"
    else:
        return "Outside"


print(hypersphere_check([1, 2, 1], 5))
print(hypersphere_check([3, 4], 5))



import numpy as np

def hypersphere_check(point, radius):

    point = np.array(point, dtype=float)

    # Compute x1² + x2² + ... + xn²
    distance_squared = np.sum(point**2)

    if distance_squared < radius**2:
        return "Inside"
    elif distance_squared == radius**2:
        return "On boundary"
    else:
        return "Outside"


print(hypersphere_check([1, 2, 1], 5))   # 3D
print(hypersphere_check([3, 4], 5))      # 2D