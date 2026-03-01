import numpy as np

def compute_variance(data):
    # Convert input list to NumPy array (float type)
    arr = np.array(data, dtype=float)

    # Step 1: Calculate the mean (average)
    mean = arr.mean()

    # Step 2: Subtract mean from each value
    # This gives deviation from mean
    deviations = arr - mean

    # Step 3: Square each deviation
    squared_deviations = deviations ** 2

    # Step 4: Take average of squared deviations
    # Variance = average of (xi - mean)^2
    variance = squared_deviations.mean()

    return variance


data = [2, 4, 6, 8]
print("Variance:", compute_variance(data))


# 🔹 Why It Makes Sense

# The numbers are evenly spread around 5.

# Distance from mean:

# 2 is 3 away

# 4 is 1 away

# 6 is 1 away

# 8 is 3 away

# So the average squared distance becomes 5.