import numpy as np

#in 2d space find the distance from orgin to the point

def calculate_distance(arr):
      
     coordinate= np.array(arr)
     distance=np.sqrt(np.sum(coordinate**2))
     print(distance)



calculate_distance(np.array([3,4]))     