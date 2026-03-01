# 🔥 So What NumPy Does Internally in np.cov()

# Internally, NumPy:

# Finds means

# Subtracts means

# Multiplies deviations

# Divides by (n-1)

# Exactly what we just did manually.


import numpy as np

def compute_covariance(x, y):
    
    # Step 1: Convert lists to NumPy arrays
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)

    # Step 2: Find means
    mean_x = np.mean(x)
    mean_y = np.mean(y)

    print("Mean of x:", mean_x)
    print("Mean of y:", mean_y)

    # Step 3: Subtract mean (deviations)
    x_dev = x - mean_x
    y_dev = y - mean_y

    print("Deviation of x:", x_dev)
    print("Deviation of y:", y_dev)

    # Step 4: Multiply deviations element-wise
    products = x_dev * y_dev
    print("Products:", products)

    # Step 5: Take average of products (Population covariance)
    covariance = np.mean(products)

    return covariance


# Input data
x = [2, 4, 6, 8]
y = [1, 3, 5, 7]

result = compute_covariance(x, y)
print("Population Covariance:", result)