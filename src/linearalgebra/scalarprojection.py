import numpy as np

#this the length projection or scalar projection


def scalarorlengthProjection(v,u):

    v_arr=np.array(v,dtype=float)
    u_arr=np.array(u,dtype=float)

    #    
    if np.allclose(u_arr, 0):
          raise ValueError("Cannot project onto zero vector")
    dot_product=np.dot(v_arr,u_arr)

    magnitude_u = np.linalg.norm(u_arr)
    return dot_product / magnitude_u



# Example
A = [3, 4]
B = [1, 1]

print("Scalar Projection (Distance):", scalarorlengthProjection(A, B))
