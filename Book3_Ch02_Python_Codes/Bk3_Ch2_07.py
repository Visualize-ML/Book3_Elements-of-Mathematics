
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch2_07

import numpy as np

# row vector dot product 

a_row = np.array([[1, 2, 3]])
b_row = np.array([[4, 3, 2]])

a_dot_b = np.inner(a_row, b_row)

print(a_dot_b)
print(np.inner(a_row[:], b_row[:]))
print(np.sum(a_row * b_row))

#%% column vector dot product 

a_col = np.array([[1],  [2], [3]])
b_col = np.array([[-1], [0], [1]])

a_dot_b = np.inner(a_col, b_col)
print(a_dot_b) # tensor product

print(np.sum(a_col * b_col))
