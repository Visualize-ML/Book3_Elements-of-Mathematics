# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 12:06:18 2022

@author: james
"""

import streamlit as st
import numpy as np
from sympy import latex, symbols
import plotly.graph_objects as go

#%%

with st.sidebar:
    
    st.latex('y = f(x_1, x_2) = ax_1 + bx_2 + c')
    
    a = st.slider('a: ', 
                  min_value = -2.0,
                  max_value = 2.0, 
                  step = 0.1)
    
    b = st.slider('b: ', 
                  min_value = -2.0,
                  max_value = 2.0, 
                  step = 0.1)
    
    c = st.slider('c: ', 
                  min_value = -2.0,
                  max_value = 2.0, 
                  step = 0.1)
    
#%%

x1, x2 = symbols('x1 x2')

y = a*x1 + b*x2 + c


num = 33
x1_array = np.linspace(-4,4,num)
x2_array = np.linspace(-4,4,num)
xx1,xx2 = np.meshgrid(x1_array,x2_array);

st.latex('f(x_1, x_2) = ' + latex(y))
yy = a*xx1 + b*xx2 + c

#%% surface

fig_1 = go.Figure(go.Surface(
    x = x1_array,
    y = x2_array,
    z = yy))

fig_1.update_layout(autosize=False,
                  width=800, height=800)
                  
st.plotly_chart(fig_1)

#%% contour

fig_2 = go.Figure(data =
    go.Contour(
    x = x1_array,
    y = x2_array,
    z = yy
    ))

fig_2.update_layout(autosize=False,
                  width=800, height=800)

st.plotly_chart(fig_2)