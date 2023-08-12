
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch4_04

from sympy.abc import x, y, z
expr = x**3 + 2*x**2 - x - 2

from sympy.utilities.lambdify import lambdify
f_x = lambdify(x, expr)

print(f_x(1))
