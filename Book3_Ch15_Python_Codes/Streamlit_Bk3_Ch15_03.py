###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2025
###############

import numpy as np  # 导入 numpy 用于数值计算
import matplotlib.pyplot as plt  # 导入 matplotlib 用于绘图
from matplotlib import cm  # 导入 matplotlib 的 cm 用于颜色映射
from sympy import latex, lambdify  # 导入 sympy 的 latex 和 lambdify
import streamlit as st  # 导入 streamlit 用于交互式界面
from sympy.abc import x  # 导入 sympy 的符号变量 x

## 定义函数，用于绘制割线
def plot_secant(x0, y0, x1, y1):  
    k = (y1 - y0) / (x1 - x0)  # 计算割线的斜率
    x = np.linspace(-1, 4, 100)  # 定义 x 的取值范围
    secant_y_x = k * (x - x0) + y0  # 根据割线方程计算 y 值
    plt.plot(x, secant_y_x, color='r', linewidth=0.25)  # 绘制割线

## 在 Streamlit 的侧边栏设置交互参数
with st.sidebar:  
    x0 = st.slider('Fixed point: ', min_value=0.5, max_value=1.5, step=0.1)  # 固定点的 x 坐标
    delta_x = st.slider('Delta x: ', min_value=0.01, max_value=0.5, value=0.5, step=0.01)  # 增量

## 定义目标函数
f_x = x**2  # 定义目标函数 f(x)
x_array = np.linspace(-1, 4, 100)  # 定义 x 的取值范围
f_x_fcn = lambdify(x, f_x)  # 将符号函数转换为数值函数
y_array = f_x_fcn(x_array)  # 计算目标函数在 x_array 的值

y0 = f_x_fcn(x0)  # 计算固定点 x0 的函数值
x1 = x0 + delta_x  # 计算增量后的点 x1
y1 = f_x_fcn(x1)  # 计算增量后的点 x1 的函数值

## 创建图形并绘制函数曲线和割线
fig, ax = plt.subplots(figsize=(8, 8))  # 创建图形和坐标轴
## 设置背景透明
fig.patch.set_alpha(0)  # 设置整个图形背景为透明
ax.set_facecolor('none')  # 设置坐标轴背景为透明

plt.plot(x_array, y_array, color='#00448A', linewidth=1.25)  # 绘制目标函数曲线
plt.plot(x0, y0, color='#92D050', marker='x', markersize=12)  # 绘制固定点 x0
plt.plot(x1, y1, color='#00448A', marker='x', markersize=12)  # 绘制增量点 x1

plot_secant(x0, y0, x1, y1)  # 调用函数绘制割线

plt.xlabel('X')  # 设置 x 轴标签
plt.ylabel('$y = f(x)$')  # 设置 y 轴标签
ax.set_title('$f(x) = %s$' % latex(f_x))  # 设置图形标题
ax.set_xlim(0, 2)  # 设置 x 轴范围
ax.set_ylim(-1, 4)  # 设置 y 轴范围

## 在 Streamlit 中显示图形
st.pyplot(fig)  
