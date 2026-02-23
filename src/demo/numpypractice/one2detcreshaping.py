import numpy as np


array1=np.arange(1,13)


try:
    respape= array1.reshape(2,6)
    print(respape)
except Exception:

   print("cannot reshape array to non integer dimensions")
   

print("deciding the automatic row in reshape")


aray2=np.arange(1,9,dtype=np.int32)


try:

    reshape2=aray2.reshape(-1,4) # it will automatically decide the number of rows and create 1 row and 7 columns
    print(reshape2)
except Exception as e:
    print("Error:", e)    