import numpy as np

def findtheProjectionInNdVector(v,u):

   v_arr=np.array(v)
   u_arr=np.array(u)

   #find the dot product

    # Check same dimension
   if v_arr.shape != u_arr.shape:
        raise ValueError("Vectors must have the same dimension")

    # Prevent division by zero
   if np.allclose(u_arr, 0):
        raise ValueError("Cannot project onto zero vector")

   dot_v=np.dot(v_arr,u_arr)
   dot_u=np.dot(u_arr,u_arr)

   projection=(dot_v/dot_u)*u_arr

   return projection
    

# 🔹 Example in 5D
v = [1, 2, 3, 4, 5]
u = [5, 4, 3, 2, 1]

proj = findtheProjectionInNdVector(v, u)
print("Projection:", proj)    