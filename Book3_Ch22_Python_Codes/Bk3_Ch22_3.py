
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch22_3

import numpy as np
a = [4,1]
b = [1,3]

# L2 norms
a_norm = np.linalg.norm(a)
b_norm = np.linalg.norm(b)

# dot product
a_dot_b = np.dot(a, b)

# cosine result
cos_result = a_dot_b/a_norm/b_norm

# radian to degree
# np.arccos(cos_result)*180/np.pi
angle = np.degrees(np.arccos(cos_result))

print(angle)
