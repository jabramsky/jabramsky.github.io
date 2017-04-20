# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 21:49:58 2017

@author: User
"""

import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

data = pd.read_csv('timeseries_nototals.csv')
data.head()

cleaned_data = data[(data['GVA'] > data['COE'])]

yeardata = []
yearlist = []

for y in range(1997, 2015):
    yeardata = cleaned_data[(cleaned_data['DATE'] == y)]
    lm = smf.ols(formula = 'WAGESHARE ~ SERVICE', data=yeardata).fit()
    yearlist.append((y,lm.summary()))
    
                       
for y in yearlist:
    print(y[0], ":")
    print(y[1])