
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch4_08

import itertools
 
letters = "ABC"

# Arranging all 3 elements

per = itertools.permutations(letters)
 
for val in per:
    print(val)
