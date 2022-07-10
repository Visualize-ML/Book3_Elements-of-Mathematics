
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch5_06

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,2*np.pi,100)

# parametric equation of unit circle
x1 = np.cos(t)
x2 = np.sin(t)

fig, ax = plt.subplots()
# plot the circle
plt.plot(x1,x2)
plt.show()
