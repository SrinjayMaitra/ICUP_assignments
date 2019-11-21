#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 21:42:52 2019

@author: aniruddhakj
"""
import pandas as pd
import statistics as st
    
    #Loading the CSV file into a dataframe called Growth
    Growth = pd.read_csv("income_growth.csv")
    
    chi_ls = Growth["China"].tolist()
    bra_ls = Growth["Brazil"].tolist()
    usa_ls = Growth["USA"].tolist()
    
    #China block for mean, median and standard deviation
    chi_mean = st.mean(chi_ls)
    chi_median = st.median(chi_ls)
    chistdd = st.stdev(chi_ls, chi_mean)
    
    #USA block for mean median and standard deviation
    usa_mean = st.mean(usa_ls)
    usa_median = st.median(usa_ls)
    usastdd = st.stdev(usa_ls, usa_mean)
    
    #Brazil block for mean median and standard deviation
    bra_mean = st.mean(bra_ls)
    bra_median = st.median(bra_ls)
    brastdd = st.stdev(bra_ls, bra_mean)

print(Growth)

#printing the means for all the Countries
print ( "MEANS\nChina :", chi_mean )
print ( "Brazil :" , bra_mean )
print ( "USA :" , usa_mean )


#printing the medians for all the Countries
print ( "MEDIANS\nChina :", chi_median )
print ( "Brazil :" , bra_median )
print ( "USA :" , usa_median )

#printing the stddev for all the Countries
print ( "Standard Deviation\nChina :", chistdd )
print ( "Brazil :" , brastdd )
print ( "USA :" , usastdd )

