from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



iris = pd.read_csv("../dataset/iris.csv")

print(iris.columns)

sns.boxplot(x="species",y="petal_length",data=iris)

plt.show()