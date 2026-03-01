import numpy as np

feature1=np.array([1,2,3,4])
feature2=np.array([3,4,5,6])

distance=np.sqrt(np.sum((feature1-feature2)**2)) # this is also

print(distance)

distance = np.linalg.norm(feature1 - feature2)  # this is also used to find the euclidian distance in nd space between two points

print(distance)