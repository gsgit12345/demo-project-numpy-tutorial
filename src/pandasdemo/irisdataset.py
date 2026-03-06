from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load dataset
#iris = load_iris()

iris = pd.read_csv("../dataset/iris.csv")

#print(iris.head())

# convert to dataframe
#df = pd.DataFrame(iris.data, columns=iris.feature_names)

# add target column
#df['species'] = iris.target

#print(df.head())


#print(iris.DESCR)

print(iris.shape)  # find out row and column 

#print(iris.columns)
      
print(iris["species"].value_counts() )  # catagory is not same that is imbalanced data set 


#plotting the dataset

iris.plot(kind="scatter", x="sepal_length", y="sepal_width")

plt.show()

#mapping the dataset

sns.set_style("whitegrid")

sns.FacetGrid(iris,hue="species",height=4).map(plt.scatter,"sepal_length","sepal_width").add_legend()

plt.show()