
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch4_07

import itertools
 
letters = "ABC"

# Arranging 2 elements out of 3

per = itertools.permutations(letters, 2)
 
for val in per:
    print(val)
