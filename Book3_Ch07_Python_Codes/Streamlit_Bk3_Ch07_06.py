###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2025
###############

# 导入必要的库
import numpy as np  # 导入NumPy库，用于数值计算
from sympy import lambdify, sqrt  # 从SymPy库中导入函数求值和平方根计算
from sympy.abc import x, y  # 定义符号变量x和y
import matplotlib.pyplot as plt  # 导入Matplotlib库，用于绘图
import streamlit as st  # 导入Streamlit库，用于创建交互式应用

## 定义绘制函数，用于绘制点、等距线和关系曲线
def plot_fcn(A, B, dist_AX_zz, dist_BX_zz, distance):
    fig, ax = plt.subplots()  # 创建绘图窗口
    ## 设置背景透明
    fig.patch.set_alpha(0)  # 设置整个图形背景为透明
    ax.set_facecolor('none')  # 设置坐标轴背景为透明
    plt.plot(A[0], A[1], color='k', marker='x', markersize=12)  # 绘制点A的位置
    colorbar = ax.contour(xx, yy, dist_AX_zz, levels=np.arange(0, 15 + 1), cmap='RdYlBu_r')  # 绘制以A为中心的等距线

    plt.plot(B[0], B[1], color='k', marker='x', markersize=12)  # 绘制点B的位置
    colorbar = ax.contour(xx, yy, dist_BX_zz, levels=np.arange(0, 15 + 1), cmap='RdYlBu_r')  # 绘制以B为中心的等距线

    ax.contour(xx, yy, distance, levels=0, colors='0.5')  # 绘制关系曲线

    fig.colorbar(colorbar, ax=ax)  # 添加颜色条
    plt.xlabel('x')  # 设置x轴标签
    plt.ylabel('y')  # 设置y轴标签
    plt.axhline(y=0, color='0.8', linestyle='-')  # 绘制x轴
    plt.axvline(x=0, color='0.8', linestyle='-')  # 绘制y轴
    plt.xticks(np.arange(-10, 10, step=2))  # 设置x轴刻度
    plt.yticks(np.arange(-10, 10, step=2))  # 设置y轴刻度
    plt.axis('scaled')  # 设置坐标轴比例相等

    ax.set_xlim(x_array.min(), x_array.max())  # 设置x轴范围
    ax.set_ylim(y_array.min(), y_array.max())  # 设置y轴范围
    ax.spines['top'].set_visible(False)  # 隐藏顶部边框
    ax.spines['right'].set_visible(False)  # 隐藏右侧边框
    ax.spines['bottom'].set_visible(False)  # 隐藏底部边框
    ax.spines['left'].set_visible(False)  # 隐藏左侧边框

    ax.grid(linestyle='--', linewidth=0.25, color=[0.8, 0.8, 0.8])  # 添加网格线

    return fig  # 返回绘图对象

## 设置交互界面的选项
options = (
    'AP - BP = 0',
    'AP - BP - 3 = 0',
    'AP - BP + 3 = 0',
    'AP - 2*BP = 0',
    'BP + AP - 8 = 0'
)

with st.sidebar:  # 在侧边栏设置用户交互输入
    option_i = st.selectbox('Choose a relation:', options)  # 用户选择关系表达式
    A_x = st.slider('x coordinate of A:', min_value=2.0, max_value=4.0, step=0.1)  # 点A的x坐标
    A_y = st.slider('y coordinate of A:', min_value=2.0, max_value=4.0, step=0.1)  # 点A的y坐标
    B_x = st.slider('x coordinate of B:', min_value=0.0, max_value=2.0, step=0.1)  # 点B的x坐标
    B_y = st.slider('y coordinate of B:', min_value=-2.0, max_value=-4.0, step=0.1)  # 点B的y坐标

## 定义点A和点B的坐标
A = [A_x, A_y]
B = [B_x, B_y]

st.latex('A = ' + str(A))  # 显示点A的坐标
st.latex('B = ' + str(B))  # 显示点B的坐标

## 生成网格
num = 301  # 定义网格数量
x_array = np.linspace(-8, 8, num)  # 定义x方向的网格范围
y_array = np.linspace(-8, 8, num)  # 定义y方向的网格范围
xx, yy = np.meshgrid(x_array, y_array)  # 创建二维网格

## 定义点A和点B到任意点P的距离函数
dist_AX = sqrt((x - A[0])**2 + (y - A[1])**2)  # 点A到点P的距离
dist_BX = sqrt((x - B[0])**2 + (y - B[1])**2)  # 点B到点P的距离

dist_AX_fcn = lambdify([x, y], dist_AX)  # 将点A的距离函数转换为可计算形式
dist_BX_fcn = lambdify([x, y], dist_BX)  # 将点B的距离函数转换为可计算形式

dist_AX_zz = dist_AX_fcn(xx, yy)  # 计算点A到网格上每个点的距离
dist_BX_zz = dist_BX_fcn(xx, yy)  # 计算点B到网格上每个点的距离

## 根据用户选择的关系表达式绘制结果
if option_i == 'AP - BP = 0':
    st.latex('AP - BP = 0')  # 显示选择的关系
    distance = dist_AX_zz - dist_BX_zz  # 计算关系曲线
    fig = plot_fcn(A, B, dist_AX_zz, dist_BX_zz, distance)  # 绘制图形
    st.pyplot(fig)  # 显示图形

elif option_i == 'AP - BP - 3 = 0':
    st.latex('AP - BP - 3 = 0')
    distance = dist_AX_zz - dist_BX_zz - 3
    fig = plot_fcn(A, B, dist_AX_zz, dist_BX_zz, distance)
    st.pyplot(fig)

elif option_i == 'AP - BP + 3 = 0':
    st.latex('AP - BP + 3 = 0')
    distance = dist_AX_zz - dist_BX_zz + 3
    fig = plot_fcn(A, B, dist_AX_zz, dist_BX_zz, distance)
    st.pyplot(fig)

elif option_i == 'AP - 2*BP = 0':
    st.latex('AP - 2*BP = 0')
    distance = dist_AX_zz - 2 * dist_BX_zz
    fig = plot_fcn(A, B, dist_AX_zz, dist_BX_zz, distance)
    st.pyplot(fig)

elif option_i == 'BP + AP - 8 = 0':
    st.latex('BP + AP - 8 = 0')
    distance = dist_BX_zz + dist_AX_zz - 8
    fig = plot_fcn(A, B, dist_AX_zz, dist_BX_zz, distance)
    st.pyplot(fig)
