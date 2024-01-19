
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch1_08

import numpy as np

# row vector transposed to a column vector
a_row = np.array([[1, 2, 3]])

b = a_row.T

b_col = np.array([[1],[2],[3]])

a = b_col.T
