import numpy as np


def twoVectorPointingSamedirectionUsingRatio(vector1,vector2):

    vector_array1=np.array(vector1,dtype=float)

    vector_array2=np.array(vector2,dtype=float)

         # Avoid division by zero

    if np.any(vector_array1==0):
        raise ValueError("vector valu is 0 can not divide")
    
    ratio=vector_array2/vector_array1

    print("Ratios:", ratio)

    # Check if all ratios are approximately equal

    return np.allclose(ratio,ratio[0])


# Example 1 (Same direction)
v1 = [1, 2]
v2 = [2, 4]

print("Same direction (ratio method):", twoVectorPointingSamedirectionUsingRatio(v1, v2))


v1 = [3, 4]
v2 = [4, 3]

print("Same direction (ratio method):", twoVectorPointingSamedirectionUsingRatio(v1, v2))