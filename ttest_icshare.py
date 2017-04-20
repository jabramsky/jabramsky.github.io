# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 14:26:03 2017

@author: User
"""

import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import scipy.stats as stats

data = pd.read_csv('ICshare.csv')
data.head()

earlydata = data[(data['WITHPS'] == 1)]
latedata = data[(data['WITHPS'] == 0)]

earlyperc = earlydata['ABSPCHANGE']
lateperc = latedata['ABSPCHANGE']

result = stats.ttest_ind(earlyperc,lateperc)

print(result)