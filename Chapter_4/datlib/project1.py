import pandas as pd
import numpy as np
import matplotlib.pyplot


data = pd.ExcelFile("C:\Users\gwens\OneDrive\Documents\611\Gwen_Project_Data.xlsx")
names = data.sheet_names

data_dct = {}
for name in names:
    data_dct[names] = data.parse(name)
    
print(data_dct)

#to check
#for key in data_dct:
    #val = data_dct[key]
    #print(data_dct[key])
   
#for key, val in data_dct.items():
    #print(val)
    
"""
Created on Wed Oct  7 14:04:11 2020

@author: gwens
"""

