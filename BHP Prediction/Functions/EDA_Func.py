# -*- coding: utf-8 -*-
"""
@author: abdelkarim MAJDOUB
@mail : abdelkarim.majdoub92@gmail.com
"""

import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import seaborn as sns

def half_corr_heatmap (dataframe, title=None, file=None):
    

    sns.set_style('whitegrid')
    plt.figure(figsize=(10,10))
    sns.set(font_scale=1)
    
    mask = np.zeros_like(dataframe.corr())
    mask[np.triu_indices_from(mask)] = True
    
    with sns.axes_style("white"):
        sns.heatmap(dataframe.corr(), mask=mask, annot=True, cmap= 'coolwarm')
        
    if title: plt.title(f'\n{title}\n', fontsize=18)
    plt.xlabel('')
    plt.ylabel('')
    if file: plt.savefig(file, bbox_inches= 'tight')
    plt.show();
    
    return

def corr_target(dataframe, target, title = None, file = None):
    plt.figure(figsize=(4,6))
    sns.set(font_scale=1)
    
    sns.heatmap(dataframe.corr()[[target]].sort_values(target, ascending = False)[1:], annot = True, 
                cmap = 'coolwarm')
    
    if title: plt.title(f'\n{title}\n', fontsize=18)
    plt.xlabel('')
    plt.ylabel('')
    if file: plt.savefig(file, bbox_inches= 'tight')
    plt.show();
    
    return
