# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 16:13:23 2021

@author: Abdelkarim MAJDOUB
@mail : abdelkarim.majdoub92@gmail.com
"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def data():
   
    data = pd.read_csv('Data/Cleaned_Data.csv')
    X= data[["AVG_CHOKE_SIZE_P","AVG_WHP_P","AVG_WHT_P","BORE_OIL_VOL","BORE_GAS_VOL", "BORE_WAT_VOL"]]
    y= data["AVG_DOWNHOLE_PRESSURE"].values.reshape(-1, 1)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
    
    X_scaler = StandardScaler().fit(X_train)
    y_scaler = StandardScaler().fit(y_train)
   
    X_train_scaled = X_scaler.transform(X_train)
    X_test_scaled = X_scaler.transform(X_test)
    y_train_scaled = y_scaler.transform(y_train)
    y_test_scaled = y_scaler.transform(y_test)
    
    x_train = X_train_scaled.reshape(-1,6)
    x_test = X_test_scaled.reshape(-1,6)
    y_train = y_train_scaled.reshape(-1,1)
    y_test = y_test_scaled.reshape(-1,1)
    return x_train, y_train, x_test, y_test
