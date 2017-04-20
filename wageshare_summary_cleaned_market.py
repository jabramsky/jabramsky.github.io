# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 15:11:55 2017

@author: User
"""

import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

data = pd.read_csv('timeseries_nototals.csv')
data.head()

exc_inds = (94, 95, 96)

for i in exc_inds:
    exc_data = data[(data['NUMBER'] != i)]

cleaned_data = exc_data[(exc_data['GVA'] > exc_data['COE'])]

needed_data = cleaned_data[['DATE', 'WAGESHARE', 'SERVICE']]

nonservice_data = needed_data[(needed_data['SERVICE'] == 0)]
service_data = needed_data[(needed_data['SERVICE'] == 1)]

print('Wage shares in non-service industries, whole timeseries:')
print(nonservice_data.describe())

print('Wage shares in service industries, whole timeseries:')
print(service_data.describe())

yearlist = []

for y in range(1997, 2015):
    yeardata = needed_data[(needed_data['DATE'] == y)]
    nonservice_data = yeardata[(yeardata['SERVICE'] == 0)]
    n_yearsharedata = nonservice_data[['WAGESHARE']]
    service_data = yeardata[(yeardata['SERVICE'] == 1)]
    yearsharedata = service_data[['WAGESHARE']]
    yearlist.append((y, n_yearsharedata.describe(), yearsharedata.describe()))
    
                       
for y in yearlist:
    print(y[0], ":")
    print('Non-service industries:')
    print(y[1])
    print('Service industries:')
    print(y[2])