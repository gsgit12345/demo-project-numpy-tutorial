import numpy as np


#creating random array 

randarray=np.random.rand(10)  # it always genetate float 
print(randarray)

randarray2=np.random.rand(10).astype(int)

print(randarray2)


randarray3 = np.random.randint(0, 10, size=10)
print(randarray3)

