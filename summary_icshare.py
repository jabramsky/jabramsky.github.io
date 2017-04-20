# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 13:45:53 2017

@author: User
"""

import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

data = pd.read_csv('ICshare.csv')
data.head()



earlydata = data[(data['WITHPS'] == 1)]
latedata = data[(data['WITHPS'] == 0)]

earlypercchange = earlydata[['ABSPCHANGE','ABSCHANGE']]


latepercchange = latedata[['ABSPCHANGE','ABSCHANGE']]

print('Changes in product shares 1997-2004:')
print(earlypercchange.describe())

print('Changes in product shares 2005-2012:')
print(latepercchange.describe())

