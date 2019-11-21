#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 19:00:36 2019

@author: rishabh
"""
#import pandas for file handling
import pandas as pd
#import numpy for statistical calculations
import numpy as np
from scipy import stats

IperC = pd.read_csv("per_capita_income.csv")

income = IperC["Income per Capita"].tolist()


IperCnew = IperC.sort_values(by = "Income per Capita", ascending = False)

print(IperCnew)
print(IperC.head(5))
print(IperC.tail(5))
incmean = np.mean(income) #mean of the data
incmedian = np.median(income) #median of the data

print(incmean)
print(incmedian)

#adding the new column as per problem statement
IperC['Income per Capita (,000)'] = [ x/1000 for x in IperC["Income per Capita"] ]
print(IperC)

IperC.to_csv("output.csv")
#reading the new file for mode of new code
IperC = pd.read_csv("output.csv")
income1000 = IperC["Income per Capita (,000)"].tolist()
imode = stats.mode(income1000)
print(imode)