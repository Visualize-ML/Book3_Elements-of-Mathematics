
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch4_03

from sympy import *
x,y,z = symbols('x y z')

# simplify mathematical expressions
expr_1 = sin(x)**2 - cos(x)**2
print(simplify(expr_1))

# expand polynomial expressions
expr_2 = (x + 1)**3
print(expand(expr_2))

# take a polynomial and factors it into irreducible factors
expr_3 = x**3 + 2*x**2 - x - 2
print(factor(expr_3))

# collect common powers of a term in an expression
expr_collected = collect(expr_3 - x**2 - 2*x, x)
print(expr_collected)
