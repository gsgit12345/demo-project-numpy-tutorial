import pandas as pd

import matplotlib.pyplot as pp

blood_data = ['A','B','O','A','AB','O','B','A','O','AB','A','B','O']

data=pd.DataFrame(blood_data,columns=["Blood_catagory"])

frequncy=data["Blood_catagory"].value_counts()


frequncy.plot(kind="bar")


pp.title("barachart")

pp.ylabel("frequncyofbllod")

pp.xlabel("blodgroup")

pp.show()