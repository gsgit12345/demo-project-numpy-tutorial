import numpy as np


oned=np.arange(1,25).reshape(4,6)# creating 1d array from 1 to 9

print(oned)

print("0d array")

zerod=np.array(100)

print(zerod)
print("shape of 0d array",zerod.shape)
print("ndim of 0d array",zerod.ndim)

print("reshaping 1d array into 2d array")

aray3=np.arange(1,13)

try:

   respahe=aray3.reshape(2,6)
   print(respahe)
finally:
    print("cannot reshape array to non integer dimensions")

thred=np.array([[[1,2,3],[4,5,6],[7,8,9]],
                [[10,11,12],[13,14,15],[16,17,18]],
                [[19,20,21],[22,23,24],[25,26,27]]])    

print(thred)
print("shape of 3d array",thred.shape)
print("ndim of 3d array",thred.ndim)