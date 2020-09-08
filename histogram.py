import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("automobile_database/car_cleaned.csv")

specdf = df.loc[:,['stroke','bore']] 
print(specdf.head())
specdf.plot.kde()
plt.title("Kernel Density Curve")

specdf.plot.box()
plt.title("Box Plot")

specdf.hist(column="stroke")
print specdf.stroke.describe()
print specdf.bore.describe()

#print(df.head())
#print(df.dtypes)
#print df.shape,df.columns

#print df.stroke.max()
#print df.stroke.std()
#print df.stroke.mean()
#print df.stroke[df.stroke>4]

'''
df.hist(column="stroke")
plt.xlabel("stroke",fontsize=15)
plt.ylabel("Frequency",fontsize=15)
plt.xlim([0.0,10.0])

df.plot.box()
df.plot.kde()
'''

plt.show()
