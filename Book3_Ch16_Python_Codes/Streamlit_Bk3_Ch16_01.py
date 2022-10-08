
###############
# Authored by Weisheng Jiang
# Book 4  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

import numpy as np
from sympy import lambdify, diff, exp, latex
from sympy.abc import x, y
import numpy as np
from matplotlib import pyplot as plt 
import streamlit as st
import plotly.graph_objects as go


#%%

options = ['First-order partial derivative with respect to x1',
           'First-order partial derivative with respect to x2',
           'Second-order partial derivative with respect to x1',
           'Second-order partial derivative with respect to x2']

label = 'Choose from:'

with st.sidebar:
    
    option_i = st.selectbox(label, options)


#%%

num = 301; # number of mesh grids
x_array = np.linspace(-3,3,num)
y_array = np.linspace(-3,3,num)
xx,yy = np.meshgrid(x_array,y_array)

# f_xy = x*exp(- x**2 - y**2);
f_xy =  3*(1-x)**2*exp(-(x**2) - (y+1)**2)\
    - 10*(x/5 - x**3 - y**5)*exp(-x**2-y**2)\
    - 1/3*exp(-(x+1)**2 - y**2) 

f_xy_fcn = lambdify([x,y],f_xy)

f_xy_zz = f_xy_fcn(xx,yy)

#%% partial derivative with respect to x1

df_dx = f_xy.diff(x)
df_dx_fcn = lambdify([x,y],df_dx)
df_dx_zz = df_dx_fcn(xx,yy)


#%% partial derivative with respect to x2

df_dy = f_xy.diff(y)
df_dy_fcn = lambdify([x,y],df_dy)
df_dy_zz = df_dy_fcn(xx,yy)

#%% second order partial derivative, x1

d2f_dxdx = f_xy.diff(x,2)
# d2f_dxdx = df_dx.diff(x)
d2f_dxdx_fcn = lambdify([x,y],d2f_dxdx)
d2f_dxdx_zz = d2f_dxdx_fcn(xx,yy)

#%% second order partial derivative, x2


d2f_dydy = f_xy.diff(y,2)
# d2f_dydy = df_dy.diff(y)
d2f_dydy_fcn = lambdify([x,y],d2f_dydy)
d2f_dydy_zz = d2f_dydy_fcn(xx,yy)


#%%

if option_i == 'First-order partial derivative with respect to x1':
    
    st.latex(r'\frac{\partial{f}}{\partial{x_1}}')
    
    ff = df_dx_zz

elif option_i == 'First-order partial derivative with respect to x2':
    
    st.latex(r'\frac{\partial{f}}{\partial{x_2}}')
    
    ff = df_dy_zz

elif option_i == 'Second-order partial derivative with respect to x1':
    
    st.latex(r'\frac{\partial^2{f}}{\partial{x_1^2}}')
    
    ff = d2f_dxdx_zz
    
elif option_i == 'Second-order partial derivative with respect to x2':
    
    st.latex(r'\frac{\partial^2{f}}{\partial{x_2^2}}')
    
    ff = d2f_dydy_zz




#%% Visualizations using plotly


fig_surface = go.Figure(go.Surface(
    x = x_array,
    y = y_array,
    z = ff,
    showscale=False,
    colorscale = 'RdYlBu_r'))
fig_surface.update_layout(
    autosize=True,
    width =800,
    height=600)

st.plotly_chart(fig_surface)  

#%%

fig_contour = go.Figure(data =
    go.Contour(
        z=ff,
        x=x_array, # horizontal axis
        y=y_array, # vertical axis
        colorscale = 'RdYlBu_r'
    ))
fig_contour.update_layout(
    autosize=True,
    width =600,
    height=600)

st.plotly_chart(fig_contour)  




