
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch24_1

import numpy as np

A = np.array([[1,1],
              [2,4]])

b = np.array([[35],
              [94]])

A_inv = np.linalg.inv(A)

x = A_inv@b
print(x)

x_ = np.linalg.solve(A,b)
print(x_)

from sympy import *
x1, x2 = symbols(['x1', 'x2'])
sol = solve([x1 + x2 - 35, 2*x1 + 4*x2 - 94], [x1, x2])
print(sol)

from sympy.solvers.solveset import linsolve
sol_ = linsolve([x1 + x2 - 35, 2*x1 + 4*x2 - 94], [x1, x2])
print(sol_)


