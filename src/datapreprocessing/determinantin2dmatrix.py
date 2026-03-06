import numpy as np

# Create a 2×2 matrix
A = np.array([[4, 2],
              [1, 3]])

# Matrix looks like this:
#        column0  column1
# row0      4        2
# row1      1        3

# Extract each element using row, column indexing

a = A[0, 0]   # row 0, column 0 → value = 4
b = A[0, 1]   # row 0, column 1 → value = 2
c = A[1, 0]   # row 1, column 0 → value = 1
d = A[1, 1]   # row 1, column 1 → value = 3

# Print extracted values
print("a =", a)  # 4
print("b =", b)  # 2
print("c =", c)  # 1
print("d =", d)  # 3

# Determinant formula for 2×2 matrix:
# |A| = (a*d) - (b*c)

determinant = (a * d) - (b * c)

print("Determinant =", determinant)