# -*- coding: utf-8 -*-
"""
Karoll Quijano - kquijano

ABE 651: Environmental Informatics

Assignment 06
Graphing Data with Python

"""

# Read data file and generate summary figures

import numpy as np 
import matplotlib.pyplot as plt

'''
This program uses an user input and output filename 
to generate a PDF file with three plots
 
'''

# file = Tippecanoe_River_at_Ora.Annual_Metrics
# file = Wildcat_Creek_at_Lafayette.Annual_Metrics

# User Input and Output names

file_in= input("Please type Input filename: ")
file_out= input("Please type Output filename: ")

# Open data usimg genfromtxt
data = np.genfromtxt(file_in+'.txt', names=True)

# Plot 1. Mean, maximum and minimum daily streamflow
plt.figure(figsize=(7,7))

plt.subplot(3,1,1)
plt.plot(data['Year'], data['Mean'], color='black', label= "Mean")
plt.plot(data['Year'], data['Max'], color='r', label= "Max")
plt.plot(data['Year'], data['Min'], 'b', label= "Min")
plt.legend()    
plt.xlabel("Year") 
plt.ylabel("Streamflow (cfs)") 

# Plot 2. Annual values of Tqmean
plt.subplot(3,1,2)
plt.plot(data['Year'], (data['Tqmean']*100), '*', color='black', label= "Tqmean")
plt.xlabel("Year") 
plt.ylabel("Tqmean (%)") 

# Plot 3. plot of R-B index
plt.subplot(3,1,3)
plt.bar(data['Year'], data['RBindex'], label= "RBindex")
plt.xlabel("Year") 
plt.ylabel("R-B Index (ratio)") 
plt.subplots_adjust(hspace= 0.7)

# Saves plots as pdf 
plt.savefig(file_out+'.pdf')
plt.close