import numpy as np

array1=np.array([1,2,3,4,5,6])

print("original array",array1)

arrayview=array1.view()

array1[3]=300
arrayview[0]=200

print("after changing the value",arrayview)


print("copy demo in numpy ")

array2=np.array([6,7,8,910])

print("original array",array2)
arraycopy=array2.copy()

print("copy of original array",arraycopy)



print("how we came to know that array owns the data or not ")
print("array owns the data or not:",arraycopy.flags.owndata) # it will return true because arraycopy is a copy of array2 and it owns the data
print("array owns the data or not:",arrayview.flags.owndata) # it will return false because arrayview is a view of array1 and it does not own the data

print("second way we can check that array owns the data or not")
print("array owns the data or not:",arraycopy.base is None) # it will return True because arraycopy is a copy of array2 and it does not own the data
print("array owns the data or not:",arrayview.base is None) # it will return False because arrayview is a view of array1 and it does own the data

print("third way we can check that array owns the data or not")

print(arraycopy.base) # it will return None because arraycopy is a copy of array2 and it does not own the data
print(arrayview.base) # it will return array1 because arrayview is a view of array