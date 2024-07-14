
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch4_09

# use sympy to solve
from sympy.solvers import solve
from sympy import Symbol
x = Symbol('x')
roots = solve(-x**3 + x, x)

# use numpy to solve
import numpy as np

coeff = [-1, 0, 1, 0]
roots_V2 = np.roots(coeff)
