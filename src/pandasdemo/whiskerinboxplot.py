import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = np.array([5,7,8,9,10,12,13,15,18,20,100])

Q1 = np.percentile(data,25)
Q3 = np.percentile(data,75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

lower_whisker = data[data >= lower_limit].min()
upper_whisker = data[data <= upper_limit].max()

outliers = data[(data < lower_limit) | (data > upper_limit)]

print("Q1:",Q1)
print("Q3:",Q3)
print("Lower whisker:",lower_whisker)
print("Upper whisker:",upper_whisker)
print("Outliers:",outliers)


# Boxplot
sns.boxplot(x=data)

plt.title("Box Plot with Seaborn")
plt.show()