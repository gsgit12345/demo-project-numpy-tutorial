# Now let’s implement PCA from scratch in NumPy with:
# 🔵 Example Dataset (3D → reduce to 2D)

# We create simple 3D data:


# 🔥 What Just Happened?

# 1️⃣ Centered data
# 2️⃣ Computed covariance
# 3️⃣ Found eigenvectors
# 4️⃣ Selected top variance directions
# 5️⃣ Projected data

# This is PCA.

# 🔥 Geometric Meaning

# You rotated coordinate system
# Then dropped least important axis.

# 🔥 Core Mathematical Idea Again
# 𝑍
# =
# 𝑋
# 𝑊
# Z=XW

# Where:

# X → original data

# W → principal directions

# Z → reduced representation


# 🔥 What This Code Does

# 1️⃣ Centers the data
# 2️⃣ Computes covariance matrix
# 3️⃣ Finds eigenvalues & eigenvectors
# 4️⃣ Sorts by largest variance
# 5️⃣ Projects onto top components
# 6️⃣ Reduces 3D → 2D
# 7️⃣ Calculates explained variance

# 🔥 Final Output Meaning

# Z → Reduced dataset

# W → Principal directions

# explained_variance_ratio → % information retained

# If first two components explain 95% variance → good reduction.


import numpy as np

# -------------------------------------------------------
# Step 0: Create Sample Data (n × d)
# n = 6 samples
# d = 3 features
# -------------------------------------------------------

X = np.array([
    [2.5, 2.4, 1.2],
    [0.5, 0.7, 0.3],
    [2.2, 2.9, 1.5],
    [1.9, 2.2, 1.1],
    [3.1, 3.0, 1.7],
    [2.3, 2.7, 1.3]
], dtype=float)

print("Original Data Shape:", X.shape)
print("Original Data:\n", X)


# -------------------------------------------------------
# Step 1: Compute Mean Vector (column-wise)
# μ = mean of each feature
# -------------------------------------------------------

mean = np.mean(X, axis=0)
print("\nMean Vector:\n", mean)


# -------------------------------------------------------
# Step 2: Center the Data
# X_centered = X - μ
# -------------------------------------------------------

X_centered = X - mean
print("\nCentered Data:\n", X_centered)


# -------------------------------------------------------
# Step 3: Compute Covariance Matrix
# Σ = (1/n) * X_centered^T * X_centered
# Result is (d × d)
# -------------------------------------------------------

n = X_centered.shape[0]
cov_matrix = (X_centered.T @ X_centered) / n
print("\nCovariance Matrix:\n", cov_matrix)


# -------------------------------------------------------
# Step 4: Compute Eigenvalues and Eigenvectors
# Eigenvectors = directions of maximum variance
# Eigenvalues = amount of variance in that direction
# -------------------------------------------------------

eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

print("\nEigenvalues:\n", eigenvalues)
print("\nEigenvectors:\n", eigenvectors)


# -------------------------------------------------------
# Step 5: Sort Eigenvalues (descending order)
# We want largest variance directions first
# -------------------------------------------------------

sorted_indices = np.argsort(eigenvalues)[::-1]

eigenvalues = eigenvalues[sorted_indices]
eigenvectors = eigenvectors[:, sorted_indices]

print("\nSorted Eigenvalues:\n", eigenvalues)


# -------------------------------------------------------
# Step 6: Select Top k Principal Components
# Here reduce 3D → 2D
# W is projection matrix (d × k)
# -------------------------------------------------------

k = 2
W = eigenvectors[:, :k]

print("\nProjection Matrix W:\n", W)


# -------------------------------------------------------
# Step 7: Project Data to Lower Dimension
# Z = X_centered @ W
# Result is (n × k)
# -------------------------------------------------------

Z = X_centered @ W

print("\nReduced Data Shape:", Z.shape)
print("\nReduced Data:\n", Z)


# -------------------------------------------------------
# Step 8: Explained Variance Ratio
# How much variance each component captures
# -------------------------------------------------------

explained_variance_ratio = eigenvalues / np.sum(eigenvalues)

print("\nExplained Variance Ratio:\n", explained_variance_ratio)