#plots.py

#os module allows you to access commandline 
#functions from python
import os
import pandas as pd
#math and data library
import numpy as np
import matplotlib.pyplot as plt

def plot_ts_scatter(df, s = 75, figsize = (40,20),
                    save_fig = False, pp = None):
    #gather variables from df
    plot_vars = list(df.keys())
    #cycle through each variable for x val
    for x in plot_vars:
        #cycle again for y value
        for y in plot_vars:
            #make sure that x does not equal y
            if x != y:
                fig, ax = plt.subplots(figsize = figsize)
                #Create list of years from index
                #Years will be represented by color
                if "Year" not in df.keys():
                    # create list from index
                    # convert each index value to string
                    # only include first 4 characters, which is the year
                    # create an integer from those characters
                    df["Year"]=[int(str(ind)[:4])for ind in df.index]
                
                df.plot.scatter(x = x, y = y, s = s, ax = ax,
                                c = "Year", cmap = "viridis")
                
                # Turn the text on the x-axis so that it reads vertical
                ax.tick_params(axis = "x", rotation = 90)
                # get rid of tick lines
                ax.tick_params("both", length = 0, which="both")
                if save_fig:
                    try:
                        os.mkdir("plots")
                    except:
                        pass
                    #identify directory to save figure
                    directory = "plots/" + x[:12] + " " + y[:12] + "c=Year"
                    plt.savefig(directory + str(plot_vars).replace("[","").replace("]", "")[:40] + "scatter.png")
                if pp != None: pp.savefig(fig, bbox_inches = "tight")
                        
def plot_stacked_lines(df, plot_vars, linewidth = 1, figsize = (40,20),
                       pp = None, total_var = False):
    fig, ax = plt.subplots(figsize = figsize)
    # df.plot.area()created a stack plot
    df[plot_vars].plot.area(stacked = True, linewidth = linewidth, 
                            ax = ax)
    if total_var != False:
        df[total_var].plot.line(linewidth = linewidth, ax = ax,
                                c = "k", label = total_var,
                                ls = "--")
    # place legend in top left corner of plot
    # format legend so that there are two columns of names
    ax.legend(loc = 2, ncol = 2)                                                                      

"""
Created on Tue Sep 29 10:22:42 2020

@author: gwens
"""

