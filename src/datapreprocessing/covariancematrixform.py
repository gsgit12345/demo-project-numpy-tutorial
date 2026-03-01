import numpy as np

# -----------------------------------------
# Step 0: Original Data Matrix (n × d)
# n = number of samples (rows)
# d = number of features (columns)
# -----------------------------------------

X = np.array([
    [4, 3],
    [2, 5],
    [1, 2]
], dtype=float)

print("Original Data (X):\n", X)


# -----------------------------------------
# Step 1: Compute Mean Vector (Column-wise)
# μ = mean of each feature
# axis=0 → mean across rows (column-wise)
# -----------------------------------------

mean = np.mean(X, axis=0)
print("\nMean Vector (μ):\n", mean)

# Manual explanation:
# Feature 1 mean = (4 + 2 + 1) / 3 = 7 / 3 = 2.3333
# Feature 2 mean = (3 + 5 + 2) / 3 = 10 / 3 = 3.3333


# -----------------------------------------
# Step 2: Center the Data
# X_centered = X - mean
# This subtracts mean from every row
# -----------------------------------------

X_centered = X - mean
print("\nCentered Data (X - μ):\n", X_centered)

# Expected values:
# Row1: [4 - 2.3333, 3 - 3.3333] = [1.6667, -0.3333]
# Row2: [2 - 2.3333, 5 - 3.3333] = [-0.3333, 1.6667]
# Row3: [1 - 2.3333, 2 - 3.3333] = [-1.3333, -1.3333]


# -----------------------------------------
# Step 3: Compute Covariance Matrix
# Formula:
# Σ = (1/n) * (X_centered^T @ X_centered)
# -----------------------------------------

n = X.shape[0]   # number of rows = 3

cov_matrix = (X_centered.T @ X_centered) / n
print("\nCovariance Matrix (Population):\n", cov_matrix)