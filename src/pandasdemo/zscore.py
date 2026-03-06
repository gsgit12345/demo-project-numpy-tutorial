import numpy as np

data = np.array([10,20,30,40,50])

mean = np.mean(data)
std = np.std(data)

z_score = (40 - mean) / std

print(z_score)