import numpy as np


def findSameDirectionOfTwoVectorUsingDotProduct(vector1,vector2):

    vector_array1=np.array(vector1,dtype=float)

    vector_array2=np.array(vector2,dtype=float)

    dot_product=np.dot(vector_array1,vector_array2)

    print(dot_product)

    magnitude1=np.linalg.norm(vector_array1)
    magnitude2=np.linalg.norm(vector_array2)

    cos_theta=dot_product/(magnitude1*magnitude2)

    print("costheta:",cos_theta)
        # If cos(theta) ≈ 1 → same direction
    return np.isclose(cos_theta, 1)

# Example
v1 = [1, 2]
v2 = [2, 4]

print("Same direction (angle method):", findSameDirectionOfTwoVectorUsingDotProduct(v1, v2))


# 🔥 Important

# cosθ ≈ 1 → same direction

# cosθ ≈ -1 → opposite direction

# cosθ ≈ 0 → perpendicular

# 🎯 Best Method?

# 👉 Angle method is safer and works in higher dimensions.
# 👉 Ratio method is simpler for understanding.