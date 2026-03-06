import numpy as np

#np.linalg.det)  using this we can find 
# Create 3×3 matrix
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# Extract values
a = A[0,0]   # 1
b = A[0,1]   # 2
c = A[0,2]   # 3

d = A[1,0]   # 4
e = A[1,1]   # 5
f = A[1,2]   # 6

g = A[2,0]   # 7
h = A[2,1]   # 8
i = A[2,2]   # 9

# Apply determinant formula
determinant = (
    a*(e*i - f*h)
    - b*(d*i - f*g)
    + c*(d*h - e*g)
)

print("Determinant =", determinant)