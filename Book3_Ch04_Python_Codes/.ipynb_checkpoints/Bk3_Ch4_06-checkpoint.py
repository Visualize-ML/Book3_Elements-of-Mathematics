
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch4_06

import itertools
 
letters = "ABC"

# find all combinations containing 2 letters

cmb = itertools.combinations(letters, 2)

for val in cmb:
    print(val)
