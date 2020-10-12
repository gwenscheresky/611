import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datlib.stats import *



data = pd.ExcelFile("Gwen_Project_Data.xlsx")#, sheet_name="Full data", index_col = [0,2])
names = list(data.sheet_names)
data_dct = {}

for name in names:
    #save sheet in dictionary under same name
     data_dct[name] = data.parse(name, index_col="Date")
     
     # problem: dataframe values are strings
     # solution: for each column, transfomr using pd.to_numeric
     for col, val in data_dct[name].items():
         # for each column - col - in the dataframe save under data_dct[name],
         # transform all values to numeric values. erorrs will return np.nan
         data_dct[name][col] = pd.to_numeric(val, errors = "coerce")         
print(data_dct)




for name in names:
    
    stats_dict = {}
    cov_dict = {}
    corr_dict = {}
    # drop null values or else statistics return nan result
    df = data_dct[name].dropna()
    # call column name in df for statistics that only require one variable
    for key1 in df:
        vec1 = df[key1]
        stats_dict[key1] = {}
        stats_dict[key1]["mean"] = mean(vec1)
        stats_dict[key1]["median"] = median(vec1)
        stats_dict[key1]["variance"] = variance(vec1)
        stats_dict[key1]["standard deviation"] = SD(vec1, sample = True)
        stats_dict[key1]["skewness"] = skewness(vec1, sample = True)
        stats_dict[key1]["kurtosis"] = kurtosis(vec1, sample = True)
        cov_dict[key1] = {}
        corr_dict[key1] = {}
        # call column from df for each cov/corr statistic
        for key2 in df:
            vec2 = df[key2]
            cov_dict[key1][key2] =covariance(vec1, vec2, sample = True)
            corr_dict[key1][key2] = correlation(vec1, vec2)
            
    #convert stats, cov, and corr dictionaries to pandas DataFrames
    stats_DF = pd.DataFrame(stats_dict)
    cov_DF = pd.DataFrame(cov_dict).sort_index(axis = 1)
    corr_DF = pd.DataFrame(corr_dict).sort_index(axis = 1)
    data_for_stats = pd.DataFrame(df)
    
    #output DataFrames to CSV
    stats_DF.to_csv(name + "stats.csv")
    cov_DF.to_csv(name + "covMatrix.csv")
    corr_DF.to_csv(name + "corrMatrix.csv")
    data_for_stats.to_csv(name + "cleanedData.csv")
