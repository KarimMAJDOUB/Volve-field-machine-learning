# -*- coding: utf-8 -*-
"""
@author: abdelkarim MAJDOUB
@mail : abdelkarim.majdoub92@gmail.com
"""



def half_corr_heatmap (dataframe, title=None, file=None):
    import pandas as pd
    import numpy as np
    import math
    import matplotlib.pyplot as plt
    import seaborn as sns

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


