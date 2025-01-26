###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2025
###############

# 导入所需的库
from sympy.abc import x  # 引入符号 x，用于定义多项式变量
from sympy import Poly, latex  # 用于处理多项式及生成 LaTeX 表达式
import matplotlib.pyplot as plt  # 用于绘制图形
import numpy as np  # 用于数值计算
import streamlit as st  # 用于创建交互式应用

## 创建交互式滑块，用于用户输入多项式的阶数
with st.sidebar:
    
    # 添加一个滑块，让用户选择多项式的阶数 n
    n = st.slider('Degree of a polynomial: ',  # 滑块的描述
                  min_value=2,  # 最小值
                  max_value=20,  # 最大值
                  value=10,  # 默认值
                  step=1)  # 步长

## 定义多项式表达式
expr = (x + 1)**n  # 定义多项式表达式 (x + 1)^n

# 在界面上显示多项式的公式
st.latex(expr)

# 展开多项式表达式
expr_expand = expr.expand()  # 使用 SymPy 的 expand 函数展开多项式
expr_expand = Poly(expr_expand)  # 将多项式转换为 Poly 对象

# 在界面上以 LaTeX 格式显示展开后的多项式
st.latex(latex(expr.expand()))

# 获取多项式的系数
poly_coeffs = expr_expand.coeffs()  # 获取多项式的所有系数

# 定义多项式各项的次数
degrees = np.linspace(n, 0, n + 1)  # 生成从 n 到 0 的等间隔值，表示每项的次数

## 绘制系数柱状图
fig, ax = plt.subplots()  # 创建图形和坐标轴
## 设置背景透明
fig.patch.set_alpha(0)  # 设置整个图形背景为透明
ax.set_facecolor('none')  # 设置坐标轴背景为透明
# 使用 stem 图绘制多项式系数
plt.stem(degrees, np.array(poly_coeffs, dtype=float), basefmt=" ")  # 绘制系数图

# 设置 x 轴范围
plt.xlim(0, n)  # x 轴范围从 0 到 n
plt.xticks(np.arange(0, n + 1))  # 设置 x 轴刻度为 0 到 n

# 设置 y 轴范围
y_max = max(poly_coeffs)  # 获取系数的最大值
y_max = float(y_max)  # 转换为浮点数
plt.ylim(0, y_max * 1.05)  # 设置 y 轴范围为 [0, 最大值的 105%]

# 隐藏右侧和顶部的边框
ax.spines['right'].set_visible(False)  # 隐藏右侧边框
ax.spines['top'].set_visible(False)  # 隐藏顶部边框

# 反转 x 轴，使次数从高到低排列
ax.invert_xaxis()  # 反转 x 轴

# 设置坐标轴标签
plt.xlabel('Degree')  # 设置 x 轴标签
plt.ylabel('Coefficient')  # 设置 y 轴标签

## 在 Streamlit 中显示图形
st.pyplot(fig)  # 使用 Streamlit 显示图形
