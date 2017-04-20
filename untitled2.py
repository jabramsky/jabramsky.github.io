# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 20:07:07 2017

@author: User
"""


import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

data = pd.read_csv('ICshare.csv')
data.head()

lm = smf.ols(formula = 'END ~ START', data=data).fit()

print(lm.summary())
