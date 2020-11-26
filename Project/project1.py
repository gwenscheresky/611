import pandas as pd
import numpy as np
import matplotlib.pyplot


data = pd.ExcelFile("Gwen_Project_Data.xlsx")
names = list(data.sheet_names)

data_dct = {}
for name in names:
    data_dct[names] = data.parse(name, index_col = "Date")
   
    for col, val in data_dct[name].items():
        data_dct[name][col] = pd.to_numeric(val, errors = "coerce")
        
print(data_dct)


