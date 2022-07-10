
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch9_02

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

a = 2
b = 1

x = np.linspace(-4,4,num = 201)
y = np.linspace(-4,4,num = 201)

xx,yy = np.meshgrid(x,y);

k_array = np.linspace(0,2,num = 21)
# k_array = np.linspace(0,1,num = 21)

k_array = np.linspace(0,-2,num = 21)
# k_array = np.linspace(0,-1,num = 21)

fig, ax = plt.subplots(figsize=(8, 8))

colors = plt.cm.RdYlBu(np.linspace(0,1,len(k_array)))

for i in range(0,len(k_array)):
    
    k = k_array[i]
    
    ellipse = (xx/a)**2 + (yy/b)**2 - 2*k*(xx/a)*(yy/b);
    
    color_code = colors[i,:].tolist()

    plt.contour(xx,yy,ellipse,levels = [1], colors = [color_code])

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
