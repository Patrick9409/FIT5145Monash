import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

titanic = pd.read_csv('D:/FIT5145/Week3/titanic.csv')

fun1 = {'who': {'passengers': 'count'}, 'age': {'average age': 'mean'}}
groupbyClass = titanic.groupby(['class', 'age']).agg(fun1)
#print(titanic[titanic['sex'] == 'male']['sex'])

fun2 = {'who': {'passengers': 'count'}, 'age': {'average age': 'mean', 'youngest': 'min', 'oldest': 'max'}}
groupbyClass = titanic.groupby('class').agg(fun2)
groupbyClass = groupbyClass.reset_index()
#groupbyClass.columns = groupbyClass.columns.droplevel1(0)
#groupbyClass.rename(columns = {'', 'class'}, inplace = True)
#print(groupbyClass)

myList = (80,20,64,19,56,12,88)
sum(e > 50 for e in myList)

fun3 = {'age': {'unique age count': 'unique', 'over 50s count': lambda x: sum(e > 50 for e in x)}}
groupbyClass = titanic.groupby('class').agg(fun3).reset_index()
#print(groupbyClass)

plt.plot(titanic.fare)

titanic.fare.hist(bins = 200)
plt.xlim(0, 300)
plt.ylim(0, 300)
plt.show()

titanic.boxplot(column = 'fare', by = 'class')
plt.ylim(0, 600)
plt.show()

fun = {'age': {"child count": lambda x: sum(e < 18 for e in x), "adult count": lambda x: sum(e > 50 for e in x)}}
groupbyClass = titanic.groupby('class').agg(fun)
print(groupbyClass)

df = pd.DataFrame({'Name' : ['Mike','Aaron','Brad','Steve','George','Mitchell','Shaun','Glenn','Pat','Robert','David'],
'Age' : [39,28,44,25,32,33,31,26,22,25,28],
'Runs' :[1310,662,1403,828,672,1140,655,1040,557,1030,1140]})
print(df)

plt.scatter(df['Age'], df['Runs'])
plt.show()

slope, intercept, r_value, p_value, std_err = linregress(df['Age'],df['Runs'])
line = [slope*xi + intercept for xi in df['Age']]
plt.plot(df['Age'],line,'r-', linewidth=3)
plt.scatter(df['Age'], df['Runs'])
plt.show()