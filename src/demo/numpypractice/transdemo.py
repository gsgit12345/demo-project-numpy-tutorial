import numpy as np


twod=np.array([[21,22,31],[14,15,16],[17,81,9]])

#print("before transpose ",twod)

twodtrans=twod.transpose()
#print("after transpose ",twodtrans)

#print(np.__version__)


print("transpose the 3d array")

fourdd=np.array([[
    [[21,3,4],[4,2,1]],
    [[23,31,4],[22,44,55]]
]])

#print(fourdd.shape)


#  (1, 2, 2, 3) -(0,1,2,3)
#print(fourdd.ndim)

## transposing the fourd array

transposearr=fourdd.transpose(3,1,2,0)

print(transposearr.shape)    # it will print (3,2,2,1)


print("transposed array",transposearr)

#print("ndim array",transposearr.ndim)

print(fourdd)
