
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch18_04

from sympy.abc import x, y, s, t
from sympy import *

f_xy = exp(- x**2 - y**2);

f_x_y_double_integrate = integrate(f_xy, (y, -oo, y), (x, -oo, x))
print(f_x_y_double_integrate)

f_x_y_volume = integrate(f_xy, (y, -oo, oo), (x, -oo, oo))
print(f_x_y_volume)
