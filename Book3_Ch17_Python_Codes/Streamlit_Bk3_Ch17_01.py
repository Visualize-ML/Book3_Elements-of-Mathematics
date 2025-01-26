###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2025
###############

from sympy import lambdify, diff, evalf, exp  # 导入Sympy的相关函数和工具，用于符号计算
from sympy.abc import x  # 定义符号变量x
import numpy as np  # 导入NumPy，用于数值计算
from matplotlib import pyplot as plt  # 导入Matplotlib，用于绘图
import streamlit as st  # 导入Streamlit，用于交互式应用

## 在侧边栏设置用户选择 ##
with st.sidebar:
    option_i = st.selectbox('Choose from:',  # 用户选择泰勒展开的阶数
                            ['First-order approximation',  # 一阶近似
                             'Second-order approximation'])  # 二阶近似
    x_0 = st.slider('Expansion point:',  # 设置泰勒展开点
                    min_value=-2.5,  # 最小值
                    max_value=2.5,  # 最大值
                    step=0.1)  # 步长

## 定义函数和相关参数 ##
f_x = exp(-x**2)  # 定义原函数f(x) = e^(-x^2)
x_array = np.linspace(-3, 3, 100)  # 在区间[-3, 3]生成100个x值
f_x_fcn = lambdify(x, f_x)  # 将符号函数转换为可执行函数
f_x_array = f_x_fcn(x_array)  # 计算原函数在x_array上的值

## 计算导数 ##
f_x_1_diff = diff(f_x, x)  # 计算f(x)的一阶导数
f_x_1_diff_fcn = lambdify(x, f_x_1_diff)  # 将一阶导数转换为可执行函数

f_x_2_diff = diff(f_x, x, 2)  # 计算f(x)的二阶导数
f_x_2_diff_fcn = lambdify(x, f_x_2_diff)  # 将二阶导数转换为可执行函数

## 创建图形 ##
fig, ax = plt.subplots()  # 创建绘图对象
ax.plot(x_array, f_x_array, linewidth=1.5)  # 绘制原函数f(x)
ax.set_xlabel("$\it{x}$")  # 设置x轴标签
ax.set_ylabel("$\it{f}(\it{x})$")  # 设置y轴标签

## 计算泰勒展开的近似 ##
y_0 = f_x.evalf(subs={x: x_0})  # 计算f(x_0)的值
x_t_array = np.linspace(x_0 - 0.5, x_0 + 0.5, 50)  # 生成展开点附近的x值

b = f_x_1_diff.evalf(subs={x: x_0})  # 计算f'(x_0)的值
a = f_x_2_diff.evalf(subs={x: x_0})  # 计算f''(x_0)的值

if option_i == 'First-order approximation':  # 如果选择一阶近似
    approx_f = b * (x - x_0) + y_0  # 定义一阶泰勒展开公式
    approx_f_fcn = lambdify(x, approx_f)  # 将一阶展开公式转换为可执行函数
    approx_f_array = approx_f_fcn(x_t_array)  # 计算近似值
else:  # 如果选择二阶近似
    approx_f = a / 2 * (x - x_0)**2 + b * (x - x_0) + y_0  # 定义二阶泰勒展开公式
    approx_f_fcn = lambdify(x, approx_f)  # 将二阶展开公式转换为可执行函数
    approx_f_array = approx_f_fcn(x_t_array)  # 计算近似值

if type(approx_f_array) == float:  # 如果结果是单个浮点数
    approx_f_array = approx_f_array + x_t_array * 0  # 扩展为与x_t_array相同长度的数组

## 绘制近似曲线和展开点 ##
ax.plot(x_t_array, approx_f_array, linewidth=0.25, color='r')  # 绘制近似曲线
ax.plot(x_0, y_0, marker='.', color='r', markersize=12)  # 标记展开点
ax.grid(linestyle='--', linewidth=0.25, color=[0.5, 0.5, 0.5])  # 设置网格线
ax.set_xlim(-3, 3)  # 设置x轴范围
ax.set_ylim(-0.25, 1.25)  # 设置y轴范围
## 设置背景透明
fig.patch.set_alpha(0)  # 设置整个图形背景为透明
ax.set_facecolor('none')  # 设置坐标轴背景为透明
## 使用Streamlit显示图形 ##
st.pyplot(fig)  # 在Streamlit界面显示图形
