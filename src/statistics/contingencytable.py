import pandas as pd


data={
    'Gender': ['Male','Female','Male','Female','Male','Female','Male','Female','Male','Female'],
    'Purchase': ['Yes','No','Yes','Yes','No','No','Yes','Yes','No','Yes']

}


df=pd.DataFrame(data)

#print(df)

table=pd.crosstab(df["Gender"],df["Purchase"])

print(table)


#row relative frequcny 

row_relative_frequncy=pd.crosstab(df["Gender"],df["Purchase"],normalize="index")

print(row_relative_frequncy)


column_relative_frequncy=pd.crosstab(df["Gender"],df["Purchase"],normalize="columns")

print(column_relative_frequncy)
