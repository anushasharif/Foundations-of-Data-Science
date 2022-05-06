# -*- coding: utf-8 -*-
"""
Created on Tue May 11 02:52:11 2021

@author: Muhammad
"""
import matplotlib.pyplot as plt
import statsmodels.api as sm
import pandas as pd
from pmdarima.arima import auto_arima
df = pd.read_excel('POL.xlsx')


fig=sm.graphics.tsa.plot_acf(df['Next Close'].dropna())
fig=sm.graphics.tsa.plot_pacf(df['Next Close'].dropna())
plt.show()

arima_model= auto_arima(df['Next Close'],start_p=0, d=0, start_q=0, max_p=5, max_d=1,max_q=5)
print (arima_model)
