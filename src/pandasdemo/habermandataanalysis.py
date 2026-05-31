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


print("applying the univariant on data")

sns.FacetGrid(data,hue="survival_status",height=5)\
.map(sns.distplot,"age")\
.add_legend()

# plt.show()


sns.FacetGrid(data,hue="survival_status",height=5)\
.map(sns.distplot,"operation_year")\
.add_legend()

#plt.show()

sns.FacetGrid(data,hue="survival_status",height=5)\
.map(sns.distplot,"auxillary_lymph_node")\
.add_legend()

# plt.show()


print("===========================drawing  cdf  plot ============================================")


counts1,binedges=np.histogram(status_yes["auxillary_lymph_node"],bins=10,    density=True
)

pdf1=counts1/sum(counts1)

print(pdf1)

print(binedges)

cdf1=np.cumsum(pdf1)

plt.plot(binedges[1:],pdf1)

plt.plot(binedges[1:],cdf1,label="yes")
plt.xlabel("nodes")

print("=============================================================")

counts2,binedges2=np.histogram(status_no["auxillary_lymph_node"],bins=10,    density=True
)

pdf2=counts2/sum(counts2)

print(pdf2)

print(binedges2)

cdf2=np.cumsum(pdf2)

plt.plot(binedges2[1:],pdf2)
plt.plot(binedges2[1:],cdf2,label="no")
plt.xlabel("nodes")
plt.legend()
#plt.show()

print("=============box plot ==================")

sns.boxenplot(x="survival_status",y="age",data=data)
plt.show()

sns.boxenplot(x="survival_status",y="operation_year",data=data)
plt.show()


sns.boxenplot(x="survival_status",y="auxillary_lymph_node",data=data)
plt.show()


print("==========================violin plot============================")

sns.violinplot(x="survival_status",y="auxillary_lymph_node",data=data)
plt.show()

sns.violinplot(x="survival_status",y="operation_year",data=data)
plt.show()

sns.violinplot(x="survival_status",y="age",data=data)
plt.show()


print("==========================paire plot============================")

sns.set_style("whitegrid")
sns.pairplot(data,hue="survival_status",height=6)
plt.show()