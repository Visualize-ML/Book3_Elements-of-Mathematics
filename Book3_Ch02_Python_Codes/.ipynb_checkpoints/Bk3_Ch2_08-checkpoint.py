
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch2_08

import numpy as np
a = np.array([[1, 2, 3]])
b = np.array([[4, 5, 6]])

# calculate element-wise product of row vectors
a_times_b = a*b

A = np.array([[1, 2, 3],
              [4, 5, 6]])

B = np.array([[1, 2, 3],
              [-1, 0, 1]])

# calculate element-wise product of matrices
A_times_B = A*B
