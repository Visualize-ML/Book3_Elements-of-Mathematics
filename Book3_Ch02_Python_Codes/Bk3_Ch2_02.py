
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch2_02

# define a function to calculate factorial

num = int(input("Enter an integer: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is ", factorial)
else:
    for i in range(1,num + 1):
       factorial = factorial*i
    print("The factorial of",num," is ",factorial)
