
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch14_03

def fib(n):
   if n <= 1:
       return (n)
   else:
       return (fib(n-1) + fib(n-2))

# Display n-term from Fibonacci sequence
n = 10  # number of terms
for i in range(n):
    print(fib(i))
