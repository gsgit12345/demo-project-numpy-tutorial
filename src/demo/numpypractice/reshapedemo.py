import numpy as np


onedar=np.array([1,2,3,4,5,6,7,8])

print(onedar)

print("reshaping 1d array into 2d array")
reshaped=onedar.reshape(2,4)
print(reshaped)
print("reshaping 1d array into 3d array")
reshaped2=onedar.reshape(2,2,2)
print(reshaped2)
print("reshaping 1d array into 4d array")
reshaped3=onedar.reshape(2,2,1,2)
print(reshaped3)
print("reshaping 1d array into 5d array")
reshaped4=onedar.reshape(2,1,1,2,2)
print(reshaped4)