import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

import pandas as pd

data = pd.read_csv("../dataset/haberman.csv")


data.columns=("age","operation_year","auxillary_lymph_node","survival_status")


print(data.head())   # here we are analyzing survival of the patient .who can survive and who not 

# 1= patient can survive for 5 years or more 
# 2- patient can survive less than 5 year

print(data.shape)

print(data.info())


data["survival_status"]=data["survival_status"].map({1:"yes",2:"no"})

print(data.head())

print(data.describe())


print(data["survival_status"].value_counts)
status_yes=data[data["survival_status"]=="yes"]

print(status_yes.describe())

status_no=data[data["survival_status"]=="no"]

print(status_no.describe())


print("applying the multivariant on data")


sns.jointplot(x="operation_year",y="age",data=data,kind="kde")

plt.show()

