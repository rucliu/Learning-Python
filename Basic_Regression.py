# -*- coding: utf-8 -*-
"""
Task 1:
    How to do some basic regression work in Python?

Created on Sun Jan  1 11:03:00 2017
@author: liuxinyu
@School of Finance, Renmin University of China
"""

from pandas import Series,DataFrame
import pandas as pd
import numpy as np

d=pd.read_excel('data.xlsx')

#(a)Calculate the mean/median/correlation coefficients
print('mean of unaid is',d.unaid.mean())
print('median of unaid is',d.unaid.median())
mat_of_data=d.corr()
print('Correlation coefficient matrix is as follows\n',mat_of_data)

#Basic linear regression 
N=2677
X=DataFrame({'dur':d.dur,'ncb':d.ncb,'rank':d.ran,'year':d.year,'cons':1})
y=d.unaid

def beta_ols_cal(first,last):#To define a process of calculating Beta_OLS
    A=np.dot(first.T,first)
    B=np.dot(first.T,last)
    C=np.linalg.inv(A)
    D=np.dot(B,C)
    return D
    
beta_ols=beta_ols_cal(X,y)
print('The coefficient of dur is ',beta_ols[1])
print('The coefficient of ncb is ',beta_ols[2])
print('The coefficient of rank is ',beta_ols[3])
print('The coefficient of year is ',beta_ols[4])
print('The coefficient of _constant is ',beta_ols[0])

#Calculate R-squared for the regression model
yhat=np.dot(X,beta_ols)
uhat=y-yhat
k=5
R_unc=sum(yhat**2)/sum(y**2)
R_c=1-sum(uhat**2)/sum((y-np.mean(y))**2)
R_adj=1-((1/(N-k))*sum(uhat**2))/((1/(N-1))*sum((y-np.mean(y))**2))
print('Uncentered-R is ',R_unc)
print('Centered-R is ',R_c)
print('adjusted-R is ',R_adj)