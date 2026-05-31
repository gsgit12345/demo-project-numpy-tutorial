
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import pandas as pd

# load dataset
iris = load_iris()

df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["species"] = iris.target

df["species"] = df["species"].map({
    0:"setosa",
    1:"versicolor",
    2:"virginica"
})

# violin plot
sns.violinplot(x="species", y="petal length (cm)", data=df)

plt.title("Violin Plot of Iris Dataset")
plt.show()