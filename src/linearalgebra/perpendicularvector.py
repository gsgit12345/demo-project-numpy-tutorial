import numpy as np

# We know from the picture:

# If angle = 90°, then:

# Dot product = 0
# Cosine similarity = 0


a=np.array([1,0])
b=np.array([0,1])

# find the dot product 

dot_product=np.dot(a*b)

#find the magnitude of vector

mag_a=np.linalg.norm(a)
mag_b=np.linalg.norm(b)

#cosine similiarity 

# Cosine similarity
cos_theta = dot_product / (mag_a * mag_b)
# Angle
angle_deg = np.degrees(np.arccos(cos_theta))

print("Dot Product:", dot_product)
print("Cosine Similarity:", cos_theta)
print("Angle (degrees):", angle_deg)


# Dot product:

# 1×0 + 0×1 = 0

# Then:

# cosθ = 0

# Then:

# θ = arccos(0)

# Which equals:

# 90°

# So angle is calculated, not inserted.

# 🔥 Very Important Understanding

# Angle comes from:

# cosθ = (a · b) / (||a|| ||b||)

# If dot product is zero → cosine is zero → angle is 90°.

