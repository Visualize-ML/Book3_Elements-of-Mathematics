
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############


from sympy import lambdify, diff, evalf, sin, exp
from sympy.abc import x
import numpy as np
from matplotlib import pyplot as plt 
from matplotlib import cm
import streamlit as st

#%%

with st.sidebar:
    
    option_i = st.selectbox('Choose from:',
                            ['First-order approximation',
                             'Second-order approximation'])
    
    x_0 = st.slider('Expansion point:',
                   min_value = -2.5,
                   max_value = 2.5,
                   step = 0.1)


#%%

f_x = exp(-x**2)

x_array   = np.linspace(-3,3,100)
x_0_array = np.linspace(-2.5,2.5,21)
# f_x.evalf(subs = {x: 0})

f_x_fcn = lambdify(x,f_x)
f_x_array = f_x_fcn(x_array)

#%% plot quadratic approx for original fcn


f_x_1_diff = diff(f_x,x)
f_x_1_diff_fcn = lambdify(x,f_x_1_diff)

f_x_2_diff = diff(f_x,x,2)
f_x_2_diff_fcn = lambdify(x,f_x_2_diff)


#%%
fig, ax = plt.subplots()

ax.plot(x_array, f_x_array, linewidth = 1.5) 
ax.set_xlabel("$\it{x}$")
ax.set_ylabel("$\it{f}(\it{x})$")


y_0 = f_x.evalf(subs = {x: x_0})
x_t_array = np.linspace(x_0-0.5, x_0+0.5, 50)

b = f_x_1_diff.evalf(subs = {x: x_0})

a = f_x_2_diff.evalf(subs = {x: x_0})

if option_i == 'First-order approximation':
    
    approx_f = b*(x - x_0) + y_0
    
    approx_f_fcn = lambdify(x,approx_f)
    approx_f_array = approx_f_fcn(x_t_array)
    
else:

    approx_f = a/2*(x - x_0)**2 + b*(x - x_0) + y_0
    
    approx_f_fcn = lambdify(x,approx_f)
    approx_f_array = approx_f_fcn(x_t_array)
    
if type(approx_f_array) == float:
    approx_f_array = approx_f_array + x_t_array*0

ax.plot(x_t_array, approx_f_array, linewidth = 0.25, color = 'r') 
ax.plot(x_0,y_0,marker = '.', color = 'r',
        markersize = 12)

ax.grid(linestyle='--', linewidth=0.25, color=[0.5,0.5,0.5])
ax.set_xlim((x_array.min(),x_array.max()))

ax.set_xlim(-3,3)
ax.set_ylim(-0.25,1.25)

st.pyplot(fig)