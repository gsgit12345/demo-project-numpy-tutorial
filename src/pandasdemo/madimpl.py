import numpy as np

# Example dataset
data = np.array([10, 12, 14, 15, 100])

# ----------------------------------------
# Step 1: Compute the median of the dataset
# median(X)
# ----------------------------------------
median = np.median(data)

# ----------------------------------------
# Step 2: Compute absolute deviation
# |xi - median|
# ----------------------------------------
absolute_deviation = np.abs(data - median)

# ----------------------------------------
# Step 3: Compute median of absolute deviations
# MAD = median(|xi - median|)
# ----------------------------------------
mad = np.median(absolute_deviation)

print("Data:", data)
print("Median:", median)
print("Absolute Deviations:", absolute_deviation)
print("Median Absolute Deviation (MAD):", mad)