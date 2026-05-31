import pandas as pd
import matplotlib.pyplot as pp


data={
    'Gender': ['Male','Female','Male','Female','Male','Female','Male','Female','Male','Female'],
    'Purchase': ['Yes','No','Yes','Yes','No','No','Yes','Yes','No','Yes']

}



df=pd.DataFrame(data)


table=pd.crosstab(df["Gender"],df["Purchase"])

table.plot(kind="bar",stacked=True)

pp.xlabel("Gender")
pp.ylabel("count")

pp.title("stacked bar chart gender vs purchase")

pp.legend("purchase")

pp.show()