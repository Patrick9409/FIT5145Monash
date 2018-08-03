'''
import pandas as pd
from matplotlib import pyplot as plt
import csv



csvFile = open("D:\FIT5197\Week2\Mushroom.csv", "r")

df = pd.DataFrame({
    'Student': [264422, 264423, 264444, 259432],
    'Name': ['Steven', 'Alex', 'Bill', 'Steven'],
    'Mark': [93.5, 61.2, 78.5, 81.1]
})
df.save_csv('output.csv')


#print(df)

#print(df["Name"])
#print(df[["Name", 'Mark']])
#print(df["Name"][1])
#print(df.loc[2]) #.loc is used to select the particular row
#print(df.loc[1:3]) #select multiple rows
#print(df.loc[df["Name"] == 'Steven'])

df = pd.read_csv("output.csv", sep=',')
print(df["Name"])
df2 = df.loc[df["Name"] == "Steven"]
df2.save_scv('output1.csv')
'''

from random import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plot
import matplotlib
from titanic import *


a = np.random.randn(5, 1)
plot.boxplot(a)

#plot.boxplot()



df = pd.DataFrame({
    'Student': [264422, 264423, 264444, 259432],
    'Name': ['Steven', 'Alex', 'Bill', 'Steven'],
    'Mark': [93.5, 61.2, 78.5, 81.1]
})

#print(df['Mark'].mean())
#print(df['Mark'].sum())
#print(df.groupby("Name").mean())
print(df.groupby("Name")["Student", "Mark"].mean())
print(df.groupby("Name").mean())

fun = {
    'who':{'passengers':'count'},
    'age':{'average age':'mean'}
}
groupbyClass = titanic.groupby('class').agg(fun)
