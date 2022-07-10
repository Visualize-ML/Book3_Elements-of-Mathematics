
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch14_05

from sympy import limit_seq, Sum, lambdify, factorial
from sympy.abc import n, k
import numpy as np
from matplotlib import pyplot as plt 

seq_sum = Sum(1 / 2**k,(k, 0, n))
seq_sum = Sum(1 /((k + 1)*(k + 2)),(k, 0, n))
seq_sum = Sum(1 /factorial(k),(k, 0, n))

seq_limit = limit_seq(seq_sum, n)

seq_sum_fcn = lambdify(n,seq_sum)

seq_sum.evalf(subs={n: 5})

n_array = np.arange(0,100 + 1,1)

seq_sum_array = []

for n in n_array:
    
    seq_n = seq_sum_fcn(n)
    
    seq_sum_array.append(seq_n)

fig, ax = plt.subplots()

ax.plot(n_array,seq_sum_array,linestyle = 'None', marker = '.')

ax.set_xlabel('$k$')
ax.set_ylabel('Sum of sequence')
ax.set_xscale('log')
ax.set_ylim(0,3)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
plt.grid(True, which="both", axis='x')
plt.tight_layout()
plt.show()

