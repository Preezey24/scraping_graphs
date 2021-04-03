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
print(df[df['W']>0][['X', 'Y']])
print(df[(df['W']>0) & (df['X']>0)])

#MISSING VALUES
d = {'A':[1,2,np.nan], 'B':[5, np.nan, np.nan], 'C':[1,2,3]}
df = pd.DataFrame(d)
print(df.dropna(axis=1))
print(df.fillna(value="FILL VALUE"))
print(df['A'].fillna(value=df['A'].mean()))

#GROUPBY
data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
      'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
       'Sales':[200,120,340,124,243,350]}
df = pd.DataFrame(data)
byComp = df.groupby('Company')
print(byComp.mean())
print(byComp.max().loc[['GOOG'],['Sales']])
print(byComp.describe())

#MERGING CONCATENATING 
#refer to notebook 

#OPERATIONS
df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
print(df['col2'].value_counts())
print(df[(df['col1']>2) & (df['col2']==444)])