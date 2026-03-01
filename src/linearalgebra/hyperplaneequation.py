import numpy as np

def implementHyperplaneEquation(x,w,w0):
    """
    Computes w·x + w0
    """
    x_array=np.array(x)
    w_array=np.array(w)

    product=np.dot(x_array,w_array)+w0

    return product


# Example (3D case)
w = [2, -1, 3]
w0 = -4

x = [1, 2, 0]

value = implementHyperplaneEquation(x, w, w0)

print("w·x + w0 =", value)

# 🔵 2️⃣ What This Output Means

# If:

# value = 0 → point lies exactly on plane
# value > 0 → point on one side
# value < 0 → point on other side

# This is how classification works.

