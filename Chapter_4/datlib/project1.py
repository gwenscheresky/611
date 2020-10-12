import pandas as pd
import numpy as np
import matplotlib.pyplot


data = pd.ExcelFile("Gwen_Project_Data.xlsx")
names = list(data.sheet_names)

data_dct = {}
for name in names:
    data_dct[names] = data.parse(name, index_col = "Date")
    
print(data_dct)


