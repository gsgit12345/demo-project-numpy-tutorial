import pandas as pd 

import matplotlib.pyplot as mlt

data = ['A','A','B','C','A','D','A','B','D','C']

df=pd.DataFrame(data,columns=["catagory"])

frequency=df["catagory"].value_counts()


relative_frequcny=df["catagory"].value_counts(normalize=True)


relative_frequcny.plot(kind='pie',autopct='%1.1f%%')

mlt.title("pie chart")

mlt.ylabel("")

mlt.show()