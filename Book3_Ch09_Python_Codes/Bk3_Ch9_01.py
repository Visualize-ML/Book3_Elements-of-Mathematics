
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch9_01

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

x = np.linspace(-4,4,num = 201)
y = np.linspace(-4,4,num = 201)
m = 1
n = 1.5

xx,yy = np.meshgrid(x,y);

e_array = np.linspace(0,3,num = 31)

fig, ax = plt.subplots(figsize=(8, 8))

colors = plt.cm.RdYlBu(np.linspace(0,1,len(e_array)))

for i in range(0,len(e_array)):
    
    e = e_array[i]
    
    ellipse = yy**2 - (e**2 - 1)*xx**2 - 2*xx;
    
    color_code = colors[i,:].tolist()

    plt.contour(xx,yy,ellipse,levels = [0], colors = [color_code])

plt.axvline(x = 0, color = 'k', linestyle = '-')
plt.axhline(y = 0, color = 'k', linestyle = '-')
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlim([-4,4])
ax.set_ylim([-4,4])

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
