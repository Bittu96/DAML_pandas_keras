import pandas as pd
import numpy as np
import csv
 
with open('persons.csv', 'wb') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['Name', 'Profession'])
    filewriter.writerow(['Derek', 'Software Developer'])
    filewriter.writerow(['Steve', 'Software Developer'])
    filewriter.writerow(['Paul', 'Manager'])

df = pd.read_csv("persons.csv")
#df = pd.read_csv("persons.csv",header = 0,usecols=['Name'])
#df = pd.read_csv("persons.csv",header = 0,index_col = 'Name')
df.to_csv('new.csv')
print(df.head())
print(df.dtypes)
print df.loc(1)

#df = pd.read_csv("automobile_database/imports-85.data")
#df.to_csv('automobile_database/car.csv')
