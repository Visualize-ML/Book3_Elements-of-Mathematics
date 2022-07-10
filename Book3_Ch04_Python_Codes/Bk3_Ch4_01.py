
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch4_01

# set A: odd
A = set([1,3,5])

# set B: even
B = set([2,4,6])

# set C: less than 4
C = set([1,2,3])

# A union B
A_union_B = A.union(B) #A|B, A or B

# A intersects (meets) B
A_meet_B = A.intersection(B) #A&B, A and B

# A minus B
A_minus_B = A.difference(B) # A - B, set difference

# A union C
A_union_C = A.union(C) #A|C, A or C

# A intersects (meets) C
A_meet_C = A.intersection(C) #A&C, A and C

# A minus C
A_minus_C = A.difference(C) # A - C, set difference

# C minus A
C_minus_A = C.difference(A) # C - A, set difference
