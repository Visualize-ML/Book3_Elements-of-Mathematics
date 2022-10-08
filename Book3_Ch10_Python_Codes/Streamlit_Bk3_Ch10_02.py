
###############
# Authored by Weisheng Jiang
# Book 4  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

import numpy as np
from sympy import lambdify, diff, exp, latex, simplify, symbols
import numpy as np
import plotly.figure_factory as ff
import plotly.graph_objects as go
import streamlit as st

x1,x2 = symbols('x1 x2')
num = 301; # number of mesh grids
x1_array = np.linspace(-3,3,num)
x2_array = np.linspace(-3,3,num)
xx1,xx2 = np.meshgrid(x1_array,x2_array)

# f_xy = x*exp(- x**2 - y**2);
f_x =  3*(1-x1)**2*exp(-(x1**2) - (x2+1)**2)\
    - 10*(x1/5 - x1**3 - x2**5)*exp(-x1**2-x2**2)\
    - 1/3*exp(-(x1+1)**2 - x2**2) 

f_x_fcn = lambdify([x1,x2],f_x)
f_zz = f_x_fcn(xx1,xx2)

st.latex('f(x_1, x_2) = ' + latex(f_x))


#%% visualizations

fig_surface = go.Figure(go.Surface(
    x = x1_array,
    y = x2_array,
    z = f_zz,
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
        z=f_zz,
        x=x1_array, # horizontal axis
        y=x2_array, # vertical axis
        colorscale = 'RdYlBu_r'
    ))
fig_contour.update_layout(
    autosize=True,
    width =600,
    height=600)

st.plotly_chart(fig_contour)  