# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 13:44:34 2017

@author: User
"""

import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

data = pd.read_csv('timeseries_nototals.csv')
data.head()

lm = smf.ols(formula = 'WAGESHARE ~ SERVICE', data=data).fit()

print(lm.summary())
