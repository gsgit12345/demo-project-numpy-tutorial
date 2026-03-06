from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



iris = pd.read_csv("../dataset/iris.csv")

print(iris.columns)

sns.set_style("whitegrid")

sns.pairplot(iris,hue="species",height=3)

plt.show()