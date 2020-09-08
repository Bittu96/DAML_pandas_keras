import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import pandas as pd

df = pd.read_csv("automobile_database/car_cleaned.csv")

specdf = df.loc[:,['stroke']] 
print(specdf.head())
y = specdf.stroke

name = specdf.stroke.name

x = np.linspace(1,205,205)
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
print("r-squared:", r_value**2)
 
plt.plot(x, y, 'o', label=name,markersize = 2)
plt.plot(x, intercept + slope*x, 'r', label='LinearRegressionLine')
plt.title('linear Regression Line for '+name+' data')
plt.xlabel("lineSpace",fontsize=10)
plt.ylabel(name,fontsize=10)
plt.legend()
plt.show()