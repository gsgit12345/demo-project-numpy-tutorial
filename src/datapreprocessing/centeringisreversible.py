import numpy as np

# ------------------------------------------------------------
# Step 1: Original Data
# ------------------------------------------------------------
X = np.array([2, 4, 6], dtype=float)

print("Original Data:", X)

# ------------------------------------------------------------
# Step 2: Compute Mean
# ------------------------------------------------------------
mean = np.mean(X)

print("Mean:", mean)

# ------------------------------------------------------------
# Step 3: Center the Data
# x_centered = x - mean
# ------------------------------------------------------------
X_centered = X - mean

print("Centered Data:", X_centered)

# ------------------------------------------------------------
# Step 4: Recover Original Data
# x = x_centered + mean
# ------------------------------------------------------------
X_recovered = X_centered + mean

print("Recovered Data:", X_recovered)

# Check if recovery is correct
print("Recovery Correct?:", np.allclose(X, X_recovered))

# ------------------------------------------------------------
# Step 5: Compute Variance
# Var = (1/n) * Σ (x - mean)^2
# ------------------------------------------------------------
variance = np.mean((X - mean) ** 2)

print("Variance:", variance)


# We will show:

# 1️⃣ Centering is reversible
# 2️⃣ Variance is NOT reversible