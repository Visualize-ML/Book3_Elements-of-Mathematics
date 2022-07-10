
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch23_4

import numpy as np

A = np.array([[1,1],
              [1,1],
              [2,4],
              [2,4]])

b = np.array([[30],
              [35],
              [90],
              [110]])

x = np.linalg.inv(A.T@A)@A.T@b

print(x)
