
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch4_02_A

from sympy.abc import x,y

expr_x = x**3 + 2*x**2 - x - 2

print(expr_x.subs(x,1))

# Bk_Ch4_02_B

from sympy import cos

expr_cos_y = expr_x.subs(x,cos(y))

print(expr_cos_y)

# Bk_Ch4_02_C

from sympy import symbols

x,y = symbols('x,y')
expr_1 = x + y
print(expr_1)

x1,x2 = symbols('x1,x2')
expr_2 = x1 + x2
print(expr_2)

