import numpy as np


def findProjectionIn2d(v,u):

    v_arr=np.array(v,dtype=float)
    u_arr=np.array(u,dtype=float)

    dot_product=np.dot(v_arr,u_arr)

    dot_product_u=np.dot(u_arr,u_arr)
    projection=(dot_product/dot_product_u)*u_arr
    return projection



v=[3,4]
u=[1,1]

result = findProjectionIn2d(v, u)
print("Projection of v onto u:", result)


# v · u = 3×1 + 4×1 = 7
# u · u = 1×1 + 1×1 = 2

# So:

# (7 / 2) × [1,1] = 3.5 × [1,1]

# Output:

# [3.5 3.5]

# Your code will print:

# Projection of v onto u: [3.5 3.5]

