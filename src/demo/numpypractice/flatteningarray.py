import numpy as np

twod=np.array([[2,3,4],[4,2,3],[7,8,6]])

print("original array",twod
      )

print("flattening the array")
flattened=twod.flatten()
print(flattened)


threed=np.array([[[1,2,3],[4,2,1]],[[4,5,6],[7,8,9]]])

print("original 3d array",threed)
print("flattening the 3d array")
flattened2=threed.flatten()
print(flattened2)