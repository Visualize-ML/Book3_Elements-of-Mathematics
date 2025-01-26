
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2025
###############


from sympy import latex, lambdify, diff, sin, log, exp, series
from sympy.abc import x
import numpy as np
from matplotlib import pyplot as plt 
from matplotlib import cm
import streamlit as st

#%%

with st.sidebar:
    
    p = st.slider('Define the degree of polynomial:',
                  min_value = 1,
                  max_value = 10,
                  step = 1)
    

#%%


f_x = exp(x)
x_array = np.linspace(-2,2,100)
x_0 = 0 # expansion point

y_0 = f_x.evalf(subs = {x: x_0})

f_x_fcn = lambdify(x,f_x)
f_x_array = f_x_fcn(x_array)


#%% Visualizations

fig = plt.figure(figsize=plt.figaspect(0.5))
ax = fig.add_subplot(1, 2, 1)
## 设置背景透明
fig.patch.set_alpha(0)  # 设置整个图形背景为透明
ax.set_facecolor('none')  # 设置坐标轴背景为透明
ax.plot(x_array, f_x_array, 'k', linewidth = 1.5) 
ax.plot(x_0, y_0, 'xr', markersize = 12) 
ax.set_xlabel("$\it{x}$")
ax.set_ylabel("$\it{f}(\it{x})$")


f_series = f_x.series(x,x_0,p + 1).removeO()
# order + 1 = number of terms

f_series_fcn = lambdify(x,f_series)
f_series_array = f_series_fcn(x_array)
f_series_array = x_array*0 + f_series_array

ax.plot(x_array, f_series_array, linewidth = 1.5,
        color = 'b') 

ax.fill_between(x_array, 
                f_x_array, 
                x_array*0 + f_series_array,
                color = '#DEEAF6')

ax.grid(linestyle='--', linewidth=0.25, color=[0.5,0.5,0.5])
ax.set_xlim(x_array.min(),x_array.max())

ax.set_ylim(np.floor(f_x_array.min()),
            np.ceil(f_x_array.max()))
# ax.set_aspect('equal', 'box')
# plt.legend()
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

ax = fig.add_subplot(1, 2, 2)
## 设置背景透明
fig.patch.set_alpha(0)  # 设置整个图形背景为透明
ax.set_facecolor('none')  # 设置坐标轴背景为透明
error = f_x_array - f_series_array
ax.plot(x_array, error, 'r', linewidth = 1.5) 
ax.fill_between(x_array, 
                error, 
                color = '#DEEAF6')
plt.axhline(y=0, color='k', linestyle='--', linewidth = 0.25)
ax.set_xlabel("$\it{x}$")
ax.set_ylabel("Error")

ax.grid(linestyle='--', linewidth=0.25, color=[0.5,0.5,0.5])
ax.set_xlim(x_array.min(),x_array.max())
ax.set_ylim(-1,5)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

st.pyplot(fig)