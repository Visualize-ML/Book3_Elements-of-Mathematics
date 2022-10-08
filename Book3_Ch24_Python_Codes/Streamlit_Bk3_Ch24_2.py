
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

import numpy as np
import streamlit as st
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

num_chickens = np.array([32, 110, 71, 79, 45, 20, 56, 55, 87, 68, 87, 63, 31, 88])
num_rabbits  = np.array([22, 53, 39, 40, 25, 15, 34, 34, 52, 41, 43, 33, 24, 52])

df = pd.DataFrame(np.vstack((num_chickens,num_rabbits)).T, 
                  columns=['num_chickens', 'num_rabbits'])

#%%

with st.sidebar:
    st.latex('\hat{y} = ax + b')
    a = st.slider('a, slope:',
              min_value = 0.05,
              max_value = 1.0,
              step = 0.01)
    
    b = st.slider('b, intercept:',
              min_value = 0.0,
              max_value = 10.0,
              step = 0.1)
    
#%%

y_hat = a*num_chickens + b

SSE = np.sum((num_rabbits - y_hat)**2)

st.write('Sum of squared errors (SSE): %.2f' %SSE)

#%%

fig = px.scatter(df, x="num_chickens", y="num_rabbits", trendline="ols")

fig.add_trace(go.Scatter(x=num_chickens, y=y_hat,
                         name = 'Predicted',
                         line=dict(color='red', width=1)))

st.plotly_chart(fig)