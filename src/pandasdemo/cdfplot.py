from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np



iris = pd.read_csv("../dataset/iris.csv")

print(iris.columns)

iris_setosa = iris.loc[iris["species"] == "setosa"]
iris_versicolor = iris.loc[iris["species"] == "versicolor"]
iris_virginica = iris.loc[iris["species"] == "virginica"]

plt.plot(
    iris_setosa["petal_length"],
    np.zeros_like(iris_setosa["petal_length"]),
    "o"
)

plt.plot(
    iris_versicolor["petal_length"],
    np.zeros_like(iris_versicolor["petal_length"]),
    "o"
)

plt.plot(
    iris_virginica["petal_length"],
    np.zeros_like(iris_virginica["petal_length"]),
    "o"
)

#plt.show()


counts,bin_edgex=np.histogram(iris_setosa["petal_length"],bins=10,density=True)
pdf=counts/(sum(counts))


print(pdf)

print(bin_edgex)

#cdf plotting 
cdf=np.cumsum(pdf)
plt.plot(bin_edgex[1:],pdf)
plt.plot(bin_edgex[1:],cdf)
plt.xlabel("petal_length")

plt.ylabel("probality")

plt.show()