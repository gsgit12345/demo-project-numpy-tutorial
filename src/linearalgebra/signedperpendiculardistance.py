import numpy as np


def distance_from_plane(weigh, bias, point):
    weight_vector = np.array(weigh, dtype=float)
    point_vector = np.array(point, dtype=float)

    numerator = np.dot(weight_vector, point_vector) + bias
    denominator = np.linalg.norm(weight_vector)

    return numerator / denominator


# Example
Weight = [2, -1]
bias = -3
point = [3, 4]

distance = distance_from_plane(Weight, bias, Perpendicular)
print("Signed Distance:", distance)

# Because:

# w → weight vector

# x → input point

# b → bias

# That matches mathematical notation:

# wᵀx + b


















# 🔵 What Problem Is This Solving?

# We have a decision boundary:

# Wᵀx + b = 0

# And we have a point:

# P

# We want to know:

# 👉 How far is P from the boundary?
# 👉 And on which side is it?

# WᵀP + b

# This gives a value that tells:

# If positive → point is on positive side

# If negative → point is on negative side

# If zero → point lies on boundary

# But this is NOT yet the true geometric distance.
# 🔵 Let’s Calculate Your Example Manually

# Given:

# W = [2, -1]
# b = -3
# P = [3, 4]

# Step 1: Dot product

# 2×3 + (-1)×4
# = 6 − 4
# = 2

# Step 2: Add bias

# 2 + (-3) = -1

# Step 3: Compute magnitude of W

# √(2² + (-1)²)
# = √(4 + 1)
# = √5 ≈ 2.236

# Step 4: Divide

# Distance = -1 / 2.236 ≈ -0.447
# 🔵 What Does Result Mean?

# Distance ≈ -0.447

# Magnitude ≈ 0.447 → actual distance
# Negative sign → point is on negative side of boundary