
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############


import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import streamlit as st
from sympy import symbols, lambdify
import plotly.graph_objects as go

#%%

def mesh_square(x1_0,x2_0,r,num):
    
    # generate mesh
 
    rr = np.linspace(-r,r,num)
    xx1,xx2 = np.meshgrid(rr,rr);
 
    xx1 = xx1 + x1_0; 
    xx2 = xx2 + x2_0;
    
    return xx1, xx2, rr

def plot_surf(xx1,xx2,ff):

    norm_plt = plt.Normalize(ff.min(), ff.max())
    colors = cm.coolwarm(norm_plt(ff))

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    surf = ax.plot_surface(xx1,xx2,ff,
    facecolors=colors, shade=False)
    surf.set_facecolor((0,0,0,0))
    # z_lim = [ff.min(),ff.max()]
    # ax.plot3D([0,0],[0,0],z_lim,'k')
    plt.show()

    plt.tight_layout()
    ax.set_xlabel('$\it{x_1}$')
    ax.set_ylabel('$\it{x_2}$')
    ax.set_zlabel('$\it{f}$($\it{x_1}$,$\it{x_2}$)')


    ax.xaxis._axinfo["grid"].update({"linewidth":0.25, "linestyle" : ":"})
    ax.yaxis._axinfo["grid"].update({"linewidth":0.25, "linestyle" : ":"})
    ax.zaxis._axinfo["grid"].update({"linewidth":0.25, "linestyle" : ":"})

    plt.rcParams["font.family"] = "Times New Roman"
    plt.rcParams["font.size"] = "10"
    
    return fig

def plot_contourf(xx1,xx2,ff):
    
    fig, ax = plt.subplots()

    cntr2 = ax.contourf(xx1,xx2,ff, levels = 15, cmap="RdBu_r")

    fig.colorbar(cntr2, ax=ax)
    plt.show()

    ax.set_xlabel('$\it{x_1}$')
    ax.set_ylabel('$\it{x_2}$')

    ax.grid(linestyle='--', linewidth=0.25, color=[0.5,0.5,0.5])
    
    return fig
    
    
#%%

with st.sidebar:
    
    st.latex(r'f(x_1,x_2) = ax_1^2 + bx_1x_2 + cx_2^2 + dx_1 + ex_2 + f')
    
    a = st.slider('a',
              min_value = -2.0,
              max_value = 2.0,
              step = 0.1)
    
    b = st.slider('b',
              min_value = -2.0,
              max_value = 2.0,
              step = 0.1)
    
    c = st.slider('c',
              min_value = -2.0,
              max_value = 2.0,
              step = 0.1)
    
    d = st.slider('d',
              min_value = -2.0,
              max_value = 2.0,
              step = 0.1)
    
    e = st.slider('e',
              min_value = -2.0,
              max_value = 2.0,
              step = 0.1)
    
    f = st.slider('f',
              min_value = -2.0,
              max_value = 2.0,
              step = 0.1)
    
#%% initialization

x1, x2 = symbols('x1 x2')

x1_0  = 0;  # center of the mesh
x2_0  = 0;  # center of the mesh
r     = 2;  # radius of the mesh
num   = 30; # number of mesh grids
xx1,xx2, x1_array = mesh_square(x1_0,x2_0,r,num); # generate mesh

x2_array = x1_array

#%% Visualizations using matplotlib

f_sym = a*x1**2 + b*x1*x2 + c*x2**2 + d*x1 + e*x2 + f

f_fcn = lambdify([x1,x2],f_sym) 

ff = f_fcn(xx1,xx2);

fig_1 = plot_surf (xx1,xx2,ff)

# st.pyplot(fig_1)

fig_2 = plot_contourf (xx1,xx2,ff)

# st.pyplot(fig_2)


#%% Visualizations using plotly


fig_surface = go.Figure(go.Surface(
    x = x1_array,
    y = x2_array,
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
        x=x1_array, # horizontal axis
        y=x2_array, # vertical axis
        colorscale = 'RdYlBu_r'
    ))
fig_contour.update_layout(
    autosize=True,
    width =600,
    height=600)

st.plotly_chart(fig_contour)  

