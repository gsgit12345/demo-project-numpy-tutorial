import numpy as np

print("reshaping 1d array into 2d array")


array1=np.arange(1,13)

try:

   respahe=array1.reshape(2,6)
   print(respahe)

except Exception as e:
    print("cannot reshape array to non integer dimensions")



arr = np.arange(1, 13)
reshaped_c = arr.reshape(3, 4, order='C')
reshaped_f = arr.reshape(3, 4, order='F')

print("C order:\n", reshaped_c)
print("F order:\n", reshaped_f)