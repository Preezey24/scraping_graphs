import pandas as pd 
import numpy as np 
from numpy.random import randn

labels = ['a', 'b', 'c']
data = [10,20,30]
myDict = {'a':10, 'b':20, 'c':30}

print(pd.Series(data, labels))
print(pd.Series(myDict))

ser1 = pd.Series([1,2,3,4], ['a', 'b', 'c', 'd'])
print(ser1['b'])

np.random.seed(101)

df = pd.DataFrame(randn(4, 4), ['A', 'B', 'C', 'D'],['W', 'X', 'Y', 'Z'])
print(df['W'])

df['new'] = df['W'] + df['Z']
print(df)

print(df.drop('A', 0))
print(df.loc[['A', 'C'], ['X', 'Z']])

bool_df = df > 0 
print(df[bool_df])

print(df['W'] > 0)
print(df[df['W']>0]['X'])