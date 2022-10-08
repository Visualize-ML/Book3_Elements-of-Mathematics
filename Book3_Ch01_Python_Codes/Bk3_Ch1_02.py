
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch1_02

from mpmath import mp

mp.dps = 1000 + 1

print('print 1000 digits of pi behind decimal point')
print(mp.pi)

print('print 1000 digits of e behind decimal point')
print(mp.e)

print('print 1000 digits of sqrt(2) behind decimal point')
print(mp.sqrt(2))
