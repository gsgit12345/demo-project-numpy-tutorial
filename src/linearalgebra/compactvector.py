import numpy  as np

def compactVector(weight,input):

#    WᵀX = 0   formula
    weight_array=np.array(weight)
    input_array=np.array(input)
    #product=np.dot(weight_array ,input_array)
    product = weight_array @ input_array # you can also use like this

    return product


# Example (2D line)
W = [1, -1]
X = [2, 2]

result = compactVector(W, X)

print("W^T X =", result)

# If result = 0 → point lies on line.


# It computes:

# WᵀX = w₁x₁ + w₂x₂

# For your example:

# 1×2 + (-1)×2 = 2 − 2 = 0

# = 0 → on boundary

# 0 → one side
# < 0 → other side