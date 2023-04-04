
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch4_05

from sympy.abc import x, a
from sympy import Poly
import matplotlib.pyplot as plt
import numpy as np

for n in [4, 8, 12, 5, 9, 13, 36]:
    
    expr = (x + 1)**n
    
    expr_expand = expr.expand()
    expr_expand = Poly(expr_expand)
    
    poly_coeffs = expr_expand.coeffs()
    
    print(poly_coeffs)
    
    degrees = np.linspace(n,0,n + 1)
    
    fig, ax = plt.subplots()
    
    plt.stem(degrees, np.array(poly_coeffs, dtype=float))
    plt.xlim(0,n)
    plt.xticks(np.arange(0,n+1))
    y_max = max(poly_coeffs)
    y_max = float(y_max)
    plt.ylim(0,y_max)
    
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.invert_xaxis()
    plt.xlabel('Degree')
    plt.ylabel('Coefficient')
    plt.show()