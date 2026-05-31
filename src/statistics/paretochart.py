import pandas as pd

import matplotlib.pyplot as pp

blood_data = ['A','B','O','A','AB','O','B','A','O','AB','A','B','O']

data=pd.DataFrame(blood_data,columns=["blodgroup"])


frequncy=data["blodgroup"].value_counts().sort_values(ascending=False)

frequncy.plot(kind="bar")

pp.title("paretochart")

pp.ylabel("frequency")
pp.xlabel("bllodgroup")

pp.show()