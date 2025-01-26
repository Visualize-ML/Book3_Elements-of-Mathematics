###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2025
###############

# 导入必要的库
import matplotlib.pyplot as plt  # 用于绘图
import streamlit as st  # 用于交互式展示
import numpy as np  # 用于数值计算
from sympy.abc import x  # 定义符号变量 x
from sympy import exp, lambdify, latex  # 用于符号表达式处理和转换

## 设置 Streamlit 侧边栏，用于用户输入参数
with st.sidebar:
    st.latex(r'f(x) = a \exp(- (b(x - c))^2) + d')  # 显示函数公式
    a = st.slider('a', min_value=-2.0, max_value=2.0, step=0.1)  # 滑动条，设置参数 a
    b = st.slider('b', min_value=-2.0, max_value=2.0, step=0.1)  # 滑动条，设置参数 b
    c = st.slider('c', min_value=-2.0, max_value=2.0, step=0.1)  # 滑动条，设置参数 c
    d = st.slider('d', min_value=-2.0, max_value=2.0, step=0.1)  # 滑动条，设置参数 d

## 定义函数 f(x)
x_array = np.arange(-4, 4 + 0.01, step=0.01)  # 在区间 [-4, 4] 内生成 x 的取值
f_x = a * exp(-(b * (x - c))**2) + d  # 定义目标函数
st.latex('f(x) = ' + latex(f_x))  # 将符号表达式显示为 LaTeX 格式

## 将符号函数转换为数值函数
f_x_fcn = lambdify([x], f_x)  # 将符号表达式转换为 Python 函数
f_x_array = f_x_fcn(x_array)  # 计算目标函数的数值结果

## 绘制目标函数
fig, ax = plt.subplots()  # 创建绘图对象
## 设置背景透明
fig.patch.set_alpha(0)  # 设置整个图形背景为透明
ax.set_facecolor('none')  # 设置坐标轴背景为透明

plt.plot(x_array, f_x_array, color='#0070C0', label='f(x)')  # 绘制函数曲线
plt.xlabel('x')  # 设置 x 轴标签
plt.ylabel('y')  # 设置 y 轴标签
plt.axhline(y=0, color='k', linestyle='-')  # 添加 y=0 的水平参考线
plt.axvline(x=0, color='k', linestyle='-')  # 添加 x=0 的垂直参考线
plt.xticks(np.arange(-4, 4 + 1, step=1))  # 设置 x 轴刻度
plt.yticks(np.arange(-4, 4 + 1, step=1))  # 设置 y 轴刻度
plt.axis('scaled')  # 设置坐标轴比例

## 设置图形样式
ax.set_xlim(-4, 4)  # 设置 x 轴范围
ax.set_ylim(-4, 4)  # 设置 y 轴范围
ax.spines['top'].set_visible(False)  # 隐藏顶部边框
ax.spines['right'].set_visible(False)  # 隐藏右侧边框
ax.spines['bottom'].set_visible(False)  # 隐藏底部边框
ax.spines['left'].set_visible(False)  # 隐藏左侧边框

plt.legend()  # 显示图例
ax.grid(linestyle='--', linewidth=0.25, color=[0.5, 0.5, 0.5])  # 添加网格线

## 设置全局绘图参数
plt.rcParams["figure.figsize"] = [7.50, 3.50]  # 设置图形尺寸
plt.rcParams["figure.autolayout"] = True  # 自动布局调整

st.pyplot(fig)  # 在 Streamlit 中显示绘图
