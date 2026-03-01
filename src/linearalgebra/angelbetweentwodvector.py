import numpy as np
# Example 2D vectors
A = np.array([3, 4])
B = np.array([4, 3])

# Step 1: Dot product
dot_product = np.dot(A, B)

# Step 2: Magnitudes
norm_A = np.linalg.norm(A)
norm_B = np.linalg.norm(B)

# Step 3: Cosine of angle
cos_theta = dot_product / (norm_A * norm_B)

# Step 4: Angle in radians
theta_radians = np.arccos(cos_theta)

# Step 5: Convert to degrees
theta_degrees = np.degrees(theta_radians)

print("Dot Product:", dot_product)
print("||A||:", norm_A)
print("||B||:", norm_B)
print("Angle (radians):", theta_radians)
print("Angle (degrees):", theta_degrees)