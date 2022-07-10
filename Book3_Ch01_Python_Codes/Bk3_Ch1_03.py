
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch1_03

# A number is even if division by 2 gives a remainder of 0.
# If the remainder is 1, it is an odd number.

num = float(input("Enter a number: "))

if num.is_integer():

    if (num % 2) == 0:
       print("{0} is even ".format(int(num)))
    else:
       print("{0} is odd ".format(int(num)))

else:
    print("{0} is not an integer ".format(num))
