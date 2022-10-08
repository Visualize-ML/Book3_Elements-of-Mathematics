
###############
# Authored by Weisheng Jiang
# Book 4  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############


import numpy as np
import matplotlib.pyplot as plt
from sympy import *
import streamlit as st


#%%

with st.sidebar:
    
    num_intervals = st.slider('Number of intervals:',
                             min_value = 5,
                             max_value = 50,
                             step = 1)
#%%

x = Symbol('x')
# f_x = x**2 + x + 1
f_x = x**2
# f_x = exp(-x**2)

f_x_fcn = lambdify([x],f_x)

integral_f_x = integrate(f_x, x)
integral_f_x_fcn = lambdify([x],integral_f_x)

a = 0 # lower bound
b = 1 # upper bound

integral_a_b = integral_f_x_fcn(b) - integral_f_x_fcn(a)

integral_a_b_v2 = integrate(f_x, (x, a, b))
integral_a_b_v2 = float(integral_a_b_v2)

print('$\int_a^b  f(x)dx = %0.3f$'%integral_a_b)


#%% Visualizations


delta_x = (b - a)/num_intervals

x_array = np.linspace(a,b,num_intervals+1)
y_array = f_x_fcn(x_array)

x_array_fine = np.linspace(a,b,200)
y_array_fine = f_x_fcn(x_array_fine)


fig = plt.figure(figsize=(15,5))

# Left Riemann sum
ax = fig.add_subplot(1,3,1)

plt.plot(x_array_fine,y_array_fine,
         color = '#0070C0')

# left endpoints
x_left = x_array[:-1] 
y_left = y_array[:-1]

plt.plot(x_left,y_left,'rx',markersize=10)

# plot the rectangles
plt.bar(x_left,y_left,
        width=delta_x,
        facecolor = '#DEEAF6',
        align='edge',
        edgecolor='#B2B2B2')

ax.axvline(x = a, color = 'r', linestyle = '-')
ax.axvline(x = b, color = 'r', linestyle = '-')

left_riemann_sum = np.sum(f_x_fcn(x_left) * delta_x)

plt.title('Left Riemann sum (N = %0.0f) = %0.3f'
          %(num_intervals,left_riemann_sum))
plt.xlim((a,b))
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
plt.xlabel('x')
plt.ylabel('f(x)')

# Middle Riemann sum

ax = fig.add_subplot(1,3,2)

plt.plot(x_array_fine,y_array_fine,
         color = '#0070C0')

# middle endpoints
x_mid = (x_array[:-1] + x_array[1:])/2 
y_mid = f_x_fcn(x_mid)

plt.plot(x_mid,y_mid,'rx',markersize=10)

# plot the rectangles
plt.bar(x_mid,y_mid,
        width=delta_x,
        facecolor = '#DEEAF6',
        edgecolor='#B2B2B2')

ax.axvline(x = a, color = 'r', linestyle = '-')
ax.axvline(x = b, color = 'r', linestyle = '-')

mid_riemann_sum = np.sum(f_x_fcn(x_mid) * delta_x)

plt.title('Middle Riemann sum (N = %0.0f) = %0.3f'
          %(num_intervals,mid_riemann_sum))
plt.xlim((a,b))
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
plt.xlabel('x')
plt.ylabel('f(x)')

# Right Riemann sum

ax = fig.add_subplot(1,3,3)

plt.plot(x_array_fine,y_array_fine,
         color = '#0070C0')

# right endpoints
x_right = x_array[1:] 
y_right = f_x_fcn(x_right)

plt.plot(x_right,y_right,'rx',markersize=10)

# plot the rectangles
plt.bar(x_right,y_right,
        width = -delta_x,
        facecolor = '#DEEAF6',
        align='edge',
        edgecolor='#B2B2B2')

ax.axvline(x = a, color = 'r', linestyle = '-')
ax.axvline(x = b, color = 'r', linestyle = '-')

right_riemann_sum = np.sum(f_x_fcn(x_right) * delta_x)

plt.title('Right Riemann sum (N = %0.0f) = %0.3f'
          %(num_intervals,right_riemann_sum))
plt.xlim((a,b))
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
plt.xlabel('x')
plt.ylabel('f(x)')

st.pyplot(fig)
