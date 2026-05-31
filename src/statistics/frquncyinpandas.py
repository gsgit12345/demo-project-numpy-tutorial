import pandas as pd 

data = ['A', 'B', 'A', 'C', 'B', 'A', 'A']


data=pd.DataFrame(data,columns=["catagory"])

frequncy=data["catagory"].value_counts()

print ("frequcny in panadas",frequncy)


# relative frequcny 

relative_frequncy=data["catagory"].value_counts(normalize=True) # normalize=True → converts counts into proportions
#relative frequency = count / total

print("relative frequncy in pandas:", relative_frequncy)

