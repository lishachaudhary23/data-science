#import libs
import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as mlt
#importing data set
data=pd.read_csv('winequality-red.csv')
#basic eda
data.head(10)
pd.set_option('display.max_columns',40)
data.head()
data.tail()
data.isna().sum()
data.describe()
#in order to find null values
data1=pd.read_csv('winequality-red.csv',na_values=[0])
data1.isna().sum()
#replacing null values with mean values
mean=data["citric acid"].mean()
data['citric acid']=data["citric acid"].replace(0,mean)
data.isna().sum()
data.describe()
data.info()
#finding corr()andploting graphs
mlt.figure(figsize=(10,8))
sns.pairplot(data)

mlt.figure(figsize=(10,8))
sns.heatmap(data.corr(),annot=True)

columns=['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
       'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
       'pH', 'sulphates', 'alcohol',]
for i in columns:
    mlt.figure(figsize=(10,8))
    sns.boxplot(x=data['quality'],y=data[i])
    
mlt.figure(figsize=(10,8))    
mlt.scatter(x=data['alcohol'],y=data['quality'])    
mlt.scatter(x=data['sulphates'],y=data['quality'])
#segregating input and output
x=data.drop(['quality'],axis=1)
y=data['quality']