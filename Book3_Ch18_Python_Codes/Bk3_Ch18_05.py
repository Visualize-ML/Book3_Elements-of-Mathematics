
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch18_05

from sympy.abc import x, y, s, t
from sympy import *

f_xy = exp(- x**2 - y**2);

f_x_partial_integrate = integrate(f_xy, (y,-oo,oo))
print(f_x_partial_integrate)

f_y_partial_integrate = integrate(f_xy, (x,-oo,oo))
print(f_y_partial_integrate)
