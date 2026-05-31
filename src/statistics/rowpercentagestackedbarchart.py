import pandas as pd
import matplotlib.pyplot as pp


data={
    'Gender': ['Male','Female','Male','Female','Male','Female','Male','Female','Male','Female'],
    'Purchase': ['Yes','No','Yes','Yes','No','No','Yes','Yes','No','Yes']

}

df=pd.DataFrame(data)


frequcny=pd.crosstab(df["Gender"],df["Purchase"],normalize="index")

frequcny.plot(kind="bar",stacked=True)

pp.xlabel("Gender")
pp.ylabel("proportion")

pp.title("stacked bar chart (row percentage)gender vs purchase")

pp.legend("purchase")

pp.show()