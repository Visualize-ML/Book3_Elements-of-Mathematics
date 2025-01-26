###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2025
###############

# 导入必要的库
import streamlit as st  # 用于创建交互式应用
import numpy as np  # 用于数值计算
from sympy import latex, symbols  # 用于符号处理和公式显示
import plotly.graph_objects as go  # 用于3D绘图和等高线图

## 创建交互式输入界面
with st.sidebar:  # 在侧边栏添加滑块和公式显示

    # 显示公式
    st.latex('y = f(x_1, x_2) = ax_1 + bx_2 + c')

    # 定义参数a的滑块，范围为-2到2，步长为0.1
    a = st.slider('a: ', 
                  min_value=-2.0,
                  max_value=2.0, 
                  step=0.1)

    # 定义参数b的滑块，范围为-2到2，步长为0.1
    b = st.slider('b: ', 
                  min_value=-2.0,
                  max_value=2.0, 
                  step=0.1)

    # 定义参数c的滑块，范围为-2到2，步长为0.1
    c = st.slider('c: ', 
                  min_value=-2.0,
                  max_value=2.0, 
                  step=0.1)

## 定义公式和计算网格值
x1, x2 = symbols('x1 x2')  # 定义符号变量 x1 和 x2
y = a * x1 + b * x2 + c  # 定义线性函数公式

# 生成计算网格
num = 33  # 定义网格点数量
x1_array = np.linspace(-4, 4, num)  # 生成 x1 的线性等分点
x2_array = np.linspace(-4, 4, num)  # 生成 x2 的线性等分点
xx1, xx2 = np.meshgrid(x1_array, x2_array)  # 生成二维网格

# 显示公式的 LaTeX 形式
st.latex('f(x_1, x_2) = ' + latex(y))

# 计算网格上函数的值
yy = a * xx1 + b * xx2 + c

## 绘制3D曲面图
fig_1 = go.Figure(go.Surface(
    x=x1_array,  # 设置 x 轴数据
    y=x2_array,  # 设置 y 轴数据
    z=yy  # 设置 z 轴数据（函数值）
))

# 设置图形的布局和大小
fig_1.update_layout(
    autosize=False,
    width=800,  # 图形宽度
    height=800  # 图形高度
)

# 在 Streamlit 应用中显示 3D 曲面图
st.plotly_chart(fig_1)

## 绘制等高线图
fig_2 = go.Figure(data=go.Contour(
    x=x1_array,  # 设置 x 轴数据
    y=x2_array,  # 设置 y 轴数据
    z=yy  # 设置 z 轴数据（函数值）
))

# 设置图形的布局和大小
fig_2.update_layout(
    autosize=False,
    width=800,  # 图形宽度
    height=800  # 图形高度
)

# 在 Streamlit 应用中显示等高线图
st.plotly_chart(fig_2)
