# 🔵 1️⃣ What We Want

# Instead of:

# One point → one distance

# We want:

# Many points → many distances

# Efficiently (no loops).

# 🔵 2️⃣ Vectorized Formula

# For multiple points:

# Distance = (XW + b) / ||W||

# Where:

# X = matrix of shape (N, d)

# W = vector of shape (d,)

# b = scalar

# Output = N distances

import numpy as np

def signed_distance_multiple(weight, bias, points):
    weight = np.array(weight, dtype=float)
    points = np.array(points, dtype=float)

    numerator = np.dot(points, weight) + bias
    denominator = np.linalg.norm(weight)

    return numerator / denominator


# Example
weight = [2, -1]
bias = -3

points = [
    [3, 4],
    [1, 1],
    [5, 2],
    [0, 3]
]

distances = signed_distance_multiple(weight, bias, points)

print("Signed Distances:", distances)



# points.shape = (4, 2)
# weight.shape = (2,)

# Then:

# np.dot(points, weight)

# Computes:

# For each row:

# w₁x₁ + w₂x₂

# All at once.

# No loop needed.
# 🔵 5️⃣ What Output Means

# For each point:

# 0 → positive side
# < 0 → negative side
# = 0 → on boundary

# This is exactly how:

# Logistic regression predicts

# SVM calculates margin

# Neural networks compute linear layer output
