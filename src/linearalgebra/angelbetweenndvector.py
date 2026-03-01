import numpy as np

# Example n-dimensional vectors
A = np.array([1, 2, 3, 4])
B = np.array([2, 1, 0, 3])

# Dot Product
dot_product = np.dot(A, B)

# Magnitude (L2 norm)
norm_A = np.linalg.norm(A)
norm_B = np.linalg.norm(B)

# Cosine Similarity
cosine_similarity = dot_product / (norm_A * norm_B)

# Angle in radians
theta_radians = np.arccos(cosine_similarity)

# Convert to degrees (optional)
theta_degrees = np.degrees(theta_radians)

print("Dot Product:", dot_product)
print("||A||:", norm_A)
print("||B||:", norm_B)
print("Cosine Similarity:", cosine_similarity)
print("Angle (radians):", theta_radians)
print("Angle (degrees):", theta_degrees)