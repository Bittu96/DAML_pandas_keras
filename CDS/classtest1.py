import pandas as pd
import numpy as np
import csv
 
df = pd.read_csv("class example.xlsx")
df.to_csv('cdsdat1.csv')
print(df.head())
print(df.dtypes)
