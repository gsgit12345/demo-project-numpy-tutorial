import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Example dataset
data = np.array([5,7,8,9,10,12,13,15,18,20,25,30,35])

# Create violin plot
sns.violinplot(x=data)

plt.title("Violin Plot using Array Dataset")
plt.show()

