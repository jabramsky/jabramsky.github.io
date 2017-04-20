# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 14:39:10 2017

@author: User
"""

import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import scipy.stats as stats

data = pd.read_csv('ICshare.csv')
data.head()

lm = smf.ols('ABSPCHANGE ~ WITHPS', data=data).fit()

print(lm.summary())