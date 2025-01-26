###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2025
###############

## 导入必要的库
import numpy as np  # 导入NumPy库，用于数值计算
import matplotlib.pyplot as plt  # 导入Matplotlib库，用于绘图
import streamlit as st  # 导入Streamlit库，用于创建交互式应用

## 定义一个函数，用于绘制向量
def draw_vector(vector, RBG):  # 自定义函数，用于绘制向量
    array = np.array([[0, 0, vector[0], vector[1]]], dtype=object)  # 创建一个二维向量的数组
    X, Y, U, V = zip(*array)  # 解压向量的坐标
    plt.quiver(X, Y, U, V, angles='xy', scale_units='xy', scale=1, color=RBG)  # 使用quiver函数绘制向量

## 创建网格数据
x1 = np.arange(-25, 25 + 1, step=1)  # 生成x1的值范围，范围为-25到25，步长为1
x2 = np.arange(-25, 25 + 1, step=1)  # 生成x2的值范围，范围为-25到25，步长为1
XX1, XX2 = np.meshgrid(x1, x2)  # 创建网格点的x和y坐标
X = np.column_stack((XX1.ravel(), XX2.ravel()))  # 将网格点展开为二维数组

## 在侧边栏设置交互参数
with st.sidebar:  # 创建Streamlit侧边栏
    st.latex(r'''A = \begin{bmatrix}
    a & b\\
    c & d
    \end{bmatrix}''')  # 显示矩阵A的LaTeX公式

    a = st.slider('a', -2.0, 2.0, step=0.1, value=1.0)  # 创建滑块，用于调整矩阵A中a的值
    b = st.slider('b', -2.0, 2.0, step=0.1, value=0.0)  # 创建滑块，用于调整矩阵A中b的值
    c = st.slider('c', -2.0, 2.0, step=0.1, value=0.0)  # 创建滑块，用于调整矩阵A中c的值
    d = st.slider('d', -2.0, 2.0, step=0.1, value=1.0)  # 创建滑块，用于调整矩阵A中d的值

## 定义变换矩阵A
theta = np.pi / 6  # 定义旋转角度
A = np.array([[a, b],  # 构造矩阵A，使用侧边栏中定义的a、b、c、d的值
              [c, d]], dtype=float)

## 计算变换后的网格点
Z = X @ A.T  # 使用矩阵A对网格点X进行变换
ZZ1 = Z[:, 0].reshape((len(x1), len(x2)))  # 提取变换后网格的x坐标
ZZ2 = Z[:, 1].reshape((len(x1), len(x2)))  # 提取变换后网格的y坐标

## 绘制原始基底图形
fig_1, ax = plt.subplots()  # 创建一个图形和坐标轴
## 设置背景透明
fig_1.patch.set_alpha(0)  # 设置整个图形背景为透明
ax.set_facecolor('none')  # 设置坐标轴背景为透明
plt.plot(XX1, XX2, color=[0.2, 0.8, 0.8])  # 绘制网格线
plt.plot(XX1.T, XX2.T, color=[0.8, 0.8, 0.2])  # 绘制网格线的转置
plt.axis('scaled')  # 设置坐标轴比例
ax.set_xlim([0, 8])  # 设置x轴范围
ax.set_ylim([0, 8])  # 设置y轴范围
plt.xticks(np.arange(0, 8 + 1, step=2))  # 设置x轴刻度
plt.yticks(np.arange(0, 8 + 1, step=2))  # 设置y轴刻度
ax.spines['top'].set_visible(False)  # 隐藏上边框
ax.spines['right'].set_visible(False)  # 隐藏右边框

## 绘制变换后的基底图形
fig_2, ax = plt.subplots()  # 创建一个图形和坐标轴
## 设置背景透明
fig_2.patch.set_alpha(0)  # 设置整个图形背景为透明
ax.set_facecolor('none')  # 设置坐标轴背景为透明
plt.plot(ZZ1, ZZ2, color=[0.2, 0.8, 0.8])  # 绘制变换后的网格线
plt.plot(ZZ1.T, ZZ2.T, color=[0.8, 0.8, 0.2])  # 绘制变换后的网格线的转置
plt.axis('scaled')  # 设置坐标轴比例
ax.set_xlim([0, 8])  # 设置x轴范围
ax.set_ylim([0, 8])  # 设置y轴范围
plt.xticks(np.arange(0, 8 + 1, step=2))  # 设置x轴刻度
plt.yticks(np.arange(0, 8 + 1, step=2))  # 设置y轴刻度
ax.spines['top'].set_visible(False)  # 隐藏上边框
ax.spines['right'].set_visible(False)  # 隐藏右边框

## 在Streamlit中展示两个图形
col1, col2 = st.columns(2)  # 创建两个列容器
with col1:  # 在第一列展示原始基底图形
    st.pyplot(fig_1)
with col2:  # 在第二列展示变换后的基底图形
    st.pyplot(fig_2)
