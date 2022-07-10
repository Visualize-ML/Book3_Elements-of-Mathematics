
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch6_06

from sympy import *
from sympy.plotting import plot3d_parametric_line
import math

t = symbols('t')

# parametric equation of spiral
x1 = cos(t)
x2 = sin(t)
x3 = t

plot3d_parametric_line(x1, x2, x3, (t, 0, 8*math.pi))

