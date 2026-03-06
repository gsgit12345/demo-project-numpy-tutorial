import numpy as np

# Example dataset
data = np.array([10, 20, 30, 40, 50])

# -----------------------------------
# Step 1: Find mean (μ)
# μ = (sum of all values) / n
# -----------------------------------
mu = np.mean(data)

# -----------------------------------
# Step 2: Compute difference from mean
# (xi - μ)
# -----------------------------------
difference = data - mu

# -----------------------------------
# Step 3: Square the differences
# (xi - μ)^2
# -----------------------------------
squared_diff = difference ** 2

# -----------------------------------
# Step 4: Compute average of squared differences
# (1/n) * Σ (xi - μ)^2
# -----------------------------------
variance = np.mean(squared_diff)

# -----------------------------------
# Step 5: Take square root
# σ = √variance
# -----------------------------------
std_dev = np.sqrt(variance)

print("Mean (μ):", mu)
print("Variance:", variance)
print("Standard Deviation (σ):", std_dev)