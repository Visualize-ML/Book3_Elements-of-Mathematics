
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch4_05

from sympy.abc import x, a
from sympy import Poly, latex
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

#%%

with st.sidebar:
    
    n = st.slider('Degree of a polynomial: ',
                  min_value = 2,
                  max_value = 20,
                  value = 10,
                  step = 1)


expr = (x + 1)**n

st.latex(expr)

expr_expand = expr.expand()
expr_expand = Poly(expr_expand)

st.latex(latex(expr.expand()))

poly_coeffs = expr_expand.coeffs()


degrees = np.linspace(n,0,n + 1)

fig, ax = plt.subplots()

plt.stem(degrees, np.array(poly_coeffs, dtype=float))
plt.show()
plt.xlim(0,n)
plt.xticks(np.arange(0,n+1))
y_max = max(poly_coeffs)
y_max = float(y_max)
plt.ylim(0,y_max*1.05)

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.invert_xaxis()
plt.xlabel('Degree')
plt.ylabel('Coefficient')

st.pyplot(fig)
