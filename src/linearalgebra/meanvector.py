import numpy as np

X = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])

mean_vector = np.mean(X, axis=0)

print("Mean Vector:", mean_vector)