###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2025
###############

import numpy as np  # 导入 numpy，用于数值计算
from matplotlib import pyplot as plt  # 导入 matplotlib，用于绘图
import streamlit as st  # 导入 streamlit，用于创建交互界面

## 设置 Streamlit 侧边栏的交互控件
with st.sidebar:  
    st.latex('a_k = aq^{k}')  # 显示几何级数公式的数学表达式

    a = st.slider('a', min_value=1, max_value=5, step=1)  # 滑动条设置初始项 a 的值
    n = st.slider('k', min_value=20, max_value=50, step=5)  # 滑动条设置项数 k 的值
    q = st.slider('q', min_value=-2.0, max_value=2.0, step=0.1)  # 滑动条设置公比 q 的值

## 生成几何级数序列
GP_sequence = [a * q**i for i in range(n)]  # 使用列表推导式生成几何级数序列
index = np.arange(1, n + 1, 1)  # 生成对应的索引数组，从 1 到 n

## 创建图形并绘制几何级数
fig, ax = plt.subplots()  # 创建图形和坐标轴
## 设置背景透明
fig.patch.set_alpha(0)  # 设置整个图形背景为透明
ax.set_facecolor('none')  # 设置坐标轴背景为透明

plt.xlabel("Index, $k$")  # 设置 x 轴标签，显示索引 k
plt.ylabel("Term, $a_k$")  # 设置 y 轴标签，显示序列项 $a_k$
plt.plot(index, GP_sequence, marker='.', markersize=6, linestyle='None')  # 绘制几何级数的散点图
ax.grid(linestyle='--', linewidth=0.25, color=[0.5, 0.5, 0.5])  # 添加网格线，设置样式和颜色

## 在 Streamlit 中显示图形
st.pyplot(fig)  
