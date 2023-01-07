
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch12_01

import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(0.1, 10, 100)
x = np.linspace(0.1, 1000, 100)

#%% x log scale
f1 = 10**x1
f2 = x1
f3 = np.log(x)

fig, ax = plt.subplots()
plt.plot(x1,f1,color = 'r')
plt.plot(x1,f2,color = 'k')
plt.plot(x,f3,color = 'b')

plt.xscale("log")
plt.ylim((-0.5,10))
plt.grid()
plt.tight_layout()
ax.set_box_aspect(1)

#%% y log scale
f1 = 10**x1
f2 = x1
f3 = np.log(x1)

fig, ax = plt.subplots()
plt.plot(x1,f1,color = 'r')
plt.plot(x1,f2,color = 'k')
plt.plot(x1,f3,color = 'b')

plt.yscale("log")
plt.ylim((0.1,1000))
plt.grid()
plt.tight_layout()
ax.set_box_aspect(1)


#%% x and y log scale
x_log_1 = np.logspace(np.log10(0.1), np.log10(3), num=100,
                      endpoint=True, base=10.0)

x_log_2 = np.logspace(np.log10(0.1), np.log10(1000), num=100,
                      endpoint=True, base=10.0)

x_log_3 = np.logspace(np.log10(1), np.log10(1000), num=100,
                      endpoint=True, base=10.0)

f1 = 10**x_log_1
f2 = x_log_2
f3 = np.log(x_log_3)

fig, ax = plt.subplots()
plt.plot(x_log_1,f1,color = 'r')
plt.plot(x_log_2,f2,color = 'k')
plt.plot(x_log_3,f3,color = 'b')

plt.yscale("log")
plt.xscale("log")
plt.ylim((0.1,1000))
plt.xlim((0.1,1000))
plt.grid()
plt.tight_layout()
ax.set_box_aspect(1)
