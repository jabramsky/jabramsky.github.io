# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 15:11:55 2017

@author: User
"""

import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

data = pd.read_csv('timeseries_manuf_nototals.csv')
data.head()

cleaned_data = data[(data['GVA'] > data['COE'])]

needed_data = cleaned_data[['DATE', 'WAGESHARE', 'MANUFACTURING']]

nonservice_data = needed_data[(needed_data['MANUFACTURING'] == 0)]
service_data = needed_data[(needed_data['MANUFACTURING'] == 1)]

print('Wage shares in non-manuf. industries, whole timeseries:')
print(nonservice_data.describe())

print('Wage shares in manuf. industries, whole timeseries:')
print(service_data.describe())

yearlist = []

for y in range(1997, 2015):
    yeardata = needed_data[(needed_data['DATE'] == y)]
    nonservice_data = yeardata[(yeardata['MANUFACTURING'] == 0)]
    n_yearsharedata = nonservice_data[['WAGESHARE']]
    service_data = yeardata[(yeardata['MANUFACTURING'] == 1)]
    yearsharedata = service_data[['WAGESHARE']]
    yearlist.append((y, n_yearsharedata.describe(), yearsharedata.describe()))
    
for y in yearlist:
    print(y[0], ":")
    print('Non-manuf. industries:')
    print(y[1])
    print('Manuf. industries:')
    print(y[2])