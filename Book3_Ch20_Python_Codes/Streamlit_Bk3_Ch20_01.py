###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2025
###############

## 导入必要的库
from matplotlib import pyplot as plt  # 导入 Matplotlib 库用于绘图
import numpy as np  # 导入 NumPy 库用于数组操作
from sympy.abc import x  # 从 SymPy 中导入符号变量 x
from sympy import Poly  # 从 SymPy 中导入多项式类
import seaborn as sns  # 导入 Seaborn 库用于高级绘图
import streamlit as st  # 导入 Streamlit 库用于创建交互式 Web 应用

## 创建 Streamlit 的侧边栏控件
with st.sidebar:  # 定义侧边栏内容
    n = st.slider('Number of steps:',  # 创建滑块用于选择步数
                  min_value=2,  # 最小值为 2
                  max_value=20,  # 最大值为 20
                  step=1)  # 步进值为 1
    
    p = st.slider('Probability, p',  # 创建滑块用于选择概率 p
                  min_value=0.1,  # 最小值为 0.1
                  max_value=0.9,  # 最大值为 0.9
                  step=0.1)  # 步进值为 0.1

## 绘制概率直方图和二叉树路径

from scipy.stats import binom  # 从 SciPy 库中导入二项分布模块

x = np.arange(0, n + 1)  # 创建范围为 [0, n] 的整数数组

p_x = binom.pmf(x, n, p)  # 计算二项分布概率质量函数 (PMF)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5), gridspec_kw={'width_ratios': [3, 1]})  # 创建包含两个子图的图形
## 设置背景透明
fig.patch.set_alpha(0)  # 设置整个图形背景为透明
ax1.set_facecolor('none')  # 设置坐标轴背景为透明
ax2.set_facecolor('none')  # 设置坐标轴背景为透明

for i in np.arange(n):  # 遍历二叉树的每一层
    Nodes_y = np.linspace(-i, i, i + 1)  # 计算当前层的节点 y 坐标
    
    B_y = np.concatenate((Nodes_y + 1, Nodes_y - 1))  # 计算下一层的节点 y 坐标
    B_x = np.zeros_like(B_y) + i + 1  # 下一层的节点 x 坐标
    B = np.stack((B_x, B_y))  # 将 x 和 y 坐标堆叠成二维数组
    
    A_y = np.concatenate((Nodes_y, Nodes_y))  # 当前层的节点 y 坐标
    A_x = np.zeros_like(A_y) + i  # 当前层的节点 x 坐标
    
    x_AB = np.stack((A_x, B_x))  # 当前层到下一层的 x 坐标连接
    y_AB = np.stack((A_y, B_y))  # 当前层到下一层的 y 坐标连接

    ax1.plot(x_AB, y_AB, 'o-', color='#92D050',  # 在二叉树中绘制节点和边
             markerfacecolor='#0099FF',
             markeredgecolor=None)

locations = np.linspace(B_y.min(), B_y.max(), n + 1)  # 计算直方图的 y 坐标位置

ax1.spines['right'].set_visible(False)  # 隐藏右边框
ax1.spines['top'].set_visible(False)  # 隐藏上边框

ax1.set_xlim(0, n)  # 设置 x 轴范围
ax1.set_ylim(B_y.min() - 1, B_y.max() + 1)  # 设置 y 轴范围

ax2.barh(locations, p_x, align='center')  # 绘制概率直方图

for i, (x, y) in enumerate(zip(locations.tolist(), p_x.tolist())):  # 遍历每个直方图条目
    ax2.text(y + p_x.max() * 0.1, x, "{:.4f}".format(y))  # 在条目旁显示概率值

ax2.set_ylim(B_y.min() - 1, B_y.max() + 1)  # 设置直方图 y 轴范围
ax2.spines['right'].set_visible(False)  # 隐藏右边框
ax2.spines['top'].set_visible(False)  # 隐藏上边框

st.pyplot(fig)  # 使用 Streamlit 显示绘制的图形
