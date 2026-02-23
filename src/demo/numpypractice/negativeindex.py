import numpy as np

fourdarray=np.array([
    
    [
    [
    [

        [1,2,35,4],[0,9,9,9]
    ],
    [
        [1,2,2,2],[1,1,1,1]
    ],
    [
        [4,5,6,7],[4,3,2,1]
    ],
    [
        [1,4,2,31],[6,4,13,2]
    ]
]
]
])

#printing 5 dimensional array

print(fourdarray)
print(fourdarray.ndim)

print(fourdarray[0][0][1][1][2]) # accessing 3 from 1st row, 1st column, 1st depth, 1st row, 3rd column
