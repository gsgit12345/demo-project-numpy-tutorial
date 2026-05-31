import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data1 = np.array([5,6,7,8,9,10])
data2 = np.array([10,12,14,16,18,20])
data3 = np.array([3,4,5,6,7,8])

dataset = [data1, data2, data3]

sns.violinplot(data=dataset)

plt.title("Violin Plot for Multiple Arrays")
plt.show()