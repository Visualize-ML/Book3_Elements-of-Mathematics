
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############


# Bk3_Ch19_02

import numpy as np
from scipy.optimize import minimize, LinearConstraint, Bounds, NonlinearConstraint
import matplotlib.pyplot as plt

def obj_f(x):
    
    x1 = x[0];
    x2 = x[1];
    
    obj = -2*x1*np.exp(-x1**2 - x2**2)
    return obj

x0 = [1,1]; # initial guess
# linear_constraint = LinearConstraint([1,1],[1],[1])

def nonlinear_c(x):
    
    x1 = x[0];
    x2 = x[1];
    
    nlc = np.abs(x1) + np.abs(x2+1) - 1
    return nlc

nlc = NonlinearConstraint(nonlinear_c, -np.inf, 0)

bounds = Bounds([-1.5, -1.5], [1.5, 1.5])

res = minimize(obj_f, x0,
               method='trust-constr',
               bounds = bounds,
               constraints=[nlc])

optimized_x = res.x;

print("==== Optimal solution ====")
print(res.x)

print("==== Optimized objective ====")
print(res.fun)

# Visualization
num = 201; # number of mesh grids
rr = np.linspace(-2,2,num)
xx1,xx2 = np.meshgrid(rr,rr);

yy = obj_f(np.vstack([xx1.ravel(), xx2.ravel()])).reshape((num,num))

fig, ax = plt.subplots()

ax.contourf(xx1,xx2,yy, levels = 20, cmap="RdYlBu_r")

yy_nlc = nonlinear_c(np.vstack([xx1.ravel(), xx2.ravel()])).reshape((num,num))
ax.contour(xx1,xx2,yy_nlc, levels = [0], colors="k")

plt.plot(optimized_x[0],optimized_x[1], 'rx', markersize = 12)

ax.set_xlabel('$\it{x}_1$')
ax.set_ylabel('$\it{x}_2$')
ax.axis('square')
ax.grid(linestyle='--', linewidth=0.25, color=[0.5,0.5,0.5])
ax.set_xlim([rr.min(),rr.max()])
ax.set_ylim([rr.min(),rr.max()])
