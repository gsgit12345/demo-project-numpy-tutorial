from   collections import Counter


data=[1,1,1,2,2,3,3,4,4,5,5,6,6,6,6,7]


fre=Counter(data)

print("frequncy is :",fre)


# total observation 

total=len(data)

relative_fre={k: k/total for k,v in  fre.items()}



print("relative frequcny:", relative_fre)