
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch1_10

list1=[1, 2, 3]
list2=[4, 5, 6]
print([x + y for x, y in zip(list1, list2)])

print(list(map(lambda x,y:x+y, list1, list2)))

import numpy as np

x = np.array(list1)
y = np.array(list2)
print(x+y)

print(np.add(list1,list2))
