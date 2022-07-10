
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch8_01

from matplotlib import pyplot as plt 
from sympy import plot_implicit, symbols, Eq
x1, x2 = symbols('x1 x2')

def plot_curve(Eq_sym):

    h_plot = plot_implicit(Eq_sym, (x1, -2.5, 2.5), (x2, -2.5, 2.5),\
                           xlabel = '$\it{x_1}$', ylabel = '$\it{x_2}$') 
    h_plot.show()

#%% plot ellipses

plt.close('all')

# major axis on x1
Eq_sym = Eq(x1**2/4 + x2**2,1)
plot_curve(Eq_sym)

# major axis on x2
Eq_sym = Eq(x1**2 + x2**2/4,1)
plot_curve(Eq_sym)

# major axis on x1 with center (h,k)
Eq_sym = Eq((x1-0.5)**2/4 + (x2-0.5)**2,1)
plot_curve(Eq_sym)

# major axis on x2 with center (h,k)
Eq_sym = Eq((x1-0.5)**2 + (x2-0.5)**2/4,1)
plot_curve(Eq_sym)

# major axis rotated counter clockwise by pi/4
Eq_sym = Eq(5*x1**2/8 -3*x1*x2/4 + 5*x2**2/8,1)
plot_curve(Eq_sym)

# major axis rotated counter clockwise by 3*pi/4
Eq_sym = Eq(5*x1**2/8 +3*x1*x2/4 + 5*x2**2/8,1)
plot_curve(Eq_sym)
