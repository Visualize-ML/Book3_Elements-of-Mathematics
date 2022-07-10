
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch24_2

import numpy as np
import matplotlib.pyplot as plt

def fig_decor(ax):
    
    plt.xlabel('$x$ (number of chickens)')
    plt.ylabel('$y$ (number of rabbits)')
    
    plt.axis('scaled')
    ax.set_xlim([0, 120])
    ax.set_ylim([0, 80])
    
    plt.xticks(np.arange(0, 120 + 1, step=10))
    plt.yticks(np.arange(0, 80 + 1,  step=10))
    
    plt.minorticks_on()
    ax.grid(which='minor', linestyle=':', 
            linewidth='0.5', color=[0.8, 0.8, 0.8])
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.grid(linestyle='--', linewidth=0.25, color=[0.5,0.5,0.5])

num_chickens = np.array([32, 110, 71, 79, 45, 20, 56, 55, 87, 68, 87, 63, 31, 88])
num_rabbits  = np.array([22, 53, 39, 40, 25, 15, 34, 34, 52, 41, 43, 33, 24, 52])

#%% generate f(a, b), sum of squared errors (SSE), symbolic
from sympy.abc import a, b
from sympy import *

y_pred = a*num_chickens + b

f_ab_SSE = np.sum((num_rabbits - y_pred)**2)

f_ab_SSE = simplify(f_ab_SSE)

print(f_ab_SSE)

#%% plot f(a) versus a

a_array = np.linspace(0,0.9,40)
b_array = np.linspace(-20,36,40)

aa,bb = np.meshgrid(a_array,b_array)

f_ab_SSE_fcn = lambdify((a,b), f_ab_SSE)

SSE_matrix = f_ab_SSE_fcn(aa,bb)
# SSE_matrix = SSE_matrix.evalf()

# first-order partial differential
df_da_SSE = diff(f_ab_SSE, a)
print(df_da_SSE)

df_db_SSE = diff(f_ab_SSE, b)
print(df_db_SSE)

# solution of (a,b)

sol = solve([df_da_SSE, df_db_SSE], [a, b])

print(sol)

a_star = sol[a]
b_star = sol[b]

a_star = a_star.evalf()
b_star = b_star.evalf()

print(a_star)
print(b_star)

SSE_min = f_ab_SSE_fcn(a_star,b_star)
print(SSE_min)

fig, ax = plt.subplots(subplot_kw={'projection': '3d'})

ax.plot_wireframe(aa,bb, SSE_matrix,
                  color = [0.5,0.5,0.5],
                  linewidth = 0.25)

plt.plot(a_star, b_star, SSE_min,
         marker = 'x', markersize = 12)

colorbar = ax.contour(aa,bb, SSE_matrix,30,
             cmap = 'RdYlBu_r')

fig.colorbar(colorbar, ax=ax)

ax.set_proj_type('ortho')

ax.set_xlabel('$a$, slope')
ax.set_ylabel('$b$, intercept')
ax.set_zlabel('$Sum of squared errors')
plt.tight_layout()
ax.set_xlim(aa.min(), aa.max())
ax.set_ylim(bb.min(), bb.max())

ax.view_init(azim=-135, elev=30)

ax.grid(False)
plt.show()

fig, ax = plt.subplots()

colorbar = ax.contourf(aa,bb, SSE_matrix, 30, cmap='RdYlBu_r')
fig.colorbar(colorbar, ax=ax)
plt.plot(a_star, b_star, marker = 'x', markersize = 12)

ax.set_xlim(aa.min(), aa.max())
ax.set_ylim(bb.min(), bb.max())

ax.set_xlabel('$a$, slope')
ax.set_ylabel('$b$, intercept')
# plt.gca().set_aspect('equal', adjustable='box')

plt.show()

#%% y = ax + b model

def plot_square(x,y1,y2):
    
    if y2 > y1:
        temp = y2;
        y2 = y1;
        y1 = temp;

    d = y1 - y2;
    
    plt.fill(np.vstack((x, x + d, x + d, x)), 
             np.vstack((y2, y2, y1, y1)),
             facecolor='b', edgecolor='none',
             alpha = 0.3)

x_array = np.linspace(0,150,10)[:, None]

y_pred = a_star*x_array + b_star

fig, ax = plt.subplots()

plt.plot(x_array, y_pred, color = 'r')
plt.scatter(num_chickens, num_rabbits)

num_rabbits_predicted = a_star*num_chickens + b_star

plt.plot(np.vstack((num_chickens,num_chickens)),
         np.vstack((num_rabbits, num_rabbits_predicted)),
         color = np.array([255,182,0])/255)

plt.plot(num_chickens, num_rabbits_predicted, 
         linestyle = 'None', marker = 'x',
         markerfacecolor = 'darkorange',
         markeredgecolor = 'darkorange',
         markersize = 10)

for i in range(0,len(num_rabbits_predicted)):
    plot_square(num_chickens[i],num_rabbits[i],num_rabbits_predicted[i]); 
        
fig_decor(ax)
