import pandas as pd
import numpy as np

df = pd.read_csv("automobile_database/car.csv",na_values=['?'],header=None,names=[
'symboling',
'normalized-losses',
'make',
'fuel-type',
'aspiration',
'num-of-doors',
'body-style',
'drive-wheels',
'engine-location',
'wheel-base',
'length',
'width',
'height',
'curb-weight',
'engine-type',
'num-of-cylinders',
'engine-size',
'fuel-system',
'bore',
'stroke',
'compression-ratio',
'horsepower',
'peak-rpm',
'city-mpg',
'highway-mpg',
'price'
])
newdf = df.fillna(method='bfill')
#newdf = df.interpolate()
#newdf.to_csv('automobile_database/car_cleaned.csv')

print(newdf.head())
print(newdf.dtypes)
