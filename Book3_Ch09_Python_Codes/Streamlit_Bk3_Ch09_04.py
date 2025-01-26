###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2025
###############

# 导入必要的库
import matplotlib.pyplot as plt  # 导入Matplotlib库，用于绘制图形
import numpy as np  # 导入NumPy库，用于数值计算
import streamlit as st  # 导入Streamlit库，用于创建交互式Web应用

## 设置侧边栏参数
with st.sidebar:
    # 显示公式
    st.latex(r' \left|\frac{x_1}{a}\right|^p + \left|\frac{x_2}{b}\right|^q = 1')
    
    # 定义参数a的滑动条
    a = st.slider('a', min_value=1.0, max_value=3.0, step=0.1)
    
    # 定义参数b的滑动条
    b = st.slider('b', min_value=1.0, max_value=3.0, step=0.1)
    
    # 定义参数p的滑动条
    p = st.slider('p', min_value=0.2, max_value=3.0, step=0.1)

    # 定义参数q的滑动条
    q = st.slider('q', min_value=0.2, max_value=3.0, step=0.1)

## 在主界面显示当前的Lp规范公式
st.latex(r' \left|\frac{x_1}{%.2f}\right|^{%.2f}+ \left|\frac{x_2}{%.2f}\right|^{%.2f} = 1' 
         % (a, p, b, q))

## 定义网格
x1 = np.linspace(-2, 2, num=101)  # 定义x1的取值范围
x2 = x1  # x2的取值范围与x1相同
xx1, xx2 = np.meshgrid(x1, x2)  # 创建二维网格

## 创建绘图窗口
fig, ax = plt.subplots(figsize=(12, 12))  # 设置绘图窗口大小

## 设置背景透明
fig.patch.set_alpha(0)  # 设置整个图形背景为透明
ax.set_facecolor('none')  # 设置坐标轴背景为透明

## 计算Lp规范的值
if np.isinf(p):  # 如果p的值趋近于无穷
    zz = np.maximum(np.abs(xx1 / a), np.abs(xx2 / b))  # L∞规范
else:
    zz = ((np.abs(xx1 / a)**p) + (np.abs(xx2 / b)**q))**(1. / q)  # Lp规范

## 绘制等高线图
# 绘制Lp规范的等高线填充
ax.contourf(xx1, xx2, zz, 20, cmap='RdYlBu_r')

# 绘制Lp = 1的轮廓线
ax.contour(xx1, xx2, zz, [1], colors='k', linewidths=2)

## 添加装饰和坐标轴设置
ax.axhline(y=0, color='k', linewidth=0.25)  # 添加x轴
ax.axvline(x=0, color='k', linewidth=0.25)  # 添加y轴
ax.set_xlim(-2, 2)  # 设置x轴范围
ax.set_ylim(-2, 2)  # 设置y轴范围
ax.spines['top'].set_visible(False)  # 隐藏顶部边框
ax.spines['right'].set_visible(False)  # 隐藏右侧边框
ax.spines['bottom'].set_visible(False)  # 隐藏底部边框
ax.spines['left'].set_visible(False)  # 隐藏左侧边框
ax.set_xlabel('$x_1$')  # 设置x轴标签
ax.set_ylabel('$x_2$')  # 设置y轴标签
ax.set_aspect('equal', adjustable='box')  # 设置坐标轴比例相等

## 在Streamlit界面显示绘图
st.pyplot(fig)  # 将绘图结果嵌入到Streamlit界面中
