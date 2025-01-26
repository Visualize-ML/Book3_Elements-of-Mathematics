###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2025
###############

import numpy as np  # 导入 numpy 用于数值计算
from sympy import lambdify, diff, exp, latex  # 导入 sympy 用于符号计算
from sympy.abc import x, y  # 定义符号变量 x 和 y
from matplotlib import pyplot as plt  # 导入 matplotlib 用于绘图
import streamlit as st  # 导入 streamlit 用于交互式界面
import plotly.graph_objects as go  # 导入 plotly 用于高级可视化

## 定义侧边栏选项
options = ['First-order partial derivative with respect to x1',  # 选项：对 x1 的一阶偏导数
           'First-order partial derivative with respect to x2',  # 选项：对 x2 的一阶偏导数
           'Second-order partial derivative with respect to x1',  # 选项：对 x1 的二阶偏导数
           'Second-order partial derivative with respect to x2']  # 选项：对 x2 的二阶偏导数
label = 'Choose from:'  # 侧边栏标题

with st.sidebar:  # 创建侧边栏
    option_i = st.selectbox(label, options)  # 下拉菜单选择计算的偏导数类型

## 创建网格点
num = 301  # 网格点的数量
x_array = np.linspace(-3, 3, num)  # x 方向的网格点
y_array = np.linspace(-3, 3, num)  # y 方向的网格点
xx, yy = np.meshgrid(x_array, y_array)  # 创建网格点矩阵

## 定义目标函数 f(x, y)
f_xy = 3 * (1 - x)**2 * exp(-(x**2) - (y + 1)**2) \
       - 10 * (x / 5 - x**3 - y**5) * exp(-x**2 - y**2) \
       - 1 / 3 * exp(-(x + 1)**2 - y**2)  # 复杂函数表达式
f_xy_fcn = lambdify([x, y], f_xy)  # 将符号函数转换为数值函数
f_xy_zz = f_xy_fcn(xx, yy)  # 计算目标函数在网格点的值

## 计算偏导数
df_dx = f_xy.diff(x)  # 对 x 计算一阶偏导数
df_dx_fcn = lambdify([x, y], df_dx)  # 转换为数值函数
df_dx_zz = df_dx_fcn(xx, yy)  # 计算一阶偏导数在网格点的值

df_dy = f_xy.diff(y)  # 对 y 计算一阶偏导数
df_dy_fcn = lambdify([x, y], df_dy)  # 转换为数值函数
df_dy_zz = df_dy_fcn(xx, yy)  # 计算一阶偏导数在网格点的值

d2f_dxdx = f_xy.diff(x, 2)  # 对 x 计算二阶偏导数
d2f_dxdx_fcn = lambdify([x, y], d2f_dxdx)  # 转换为数值函数
d2f_dxdx_zz = d2f_dxdx_fcn(xx, yy)  # 计算二阶偏导数在网格点的值

d2f_dydy = f_xy.diff(y, 2)  # 对 y 计算二阶偏导数
d2f_dydy_fcn = lambdify([x, y], d2f_dydy)  # 转换为数值函数
d2f_dydy_zz = d2f_dydy_fcn(xx, yy)  # 计算二阶偏导数在网格点的值

## 根据选项选择偏导数进行可视化
if option_i == 'First-order partial derivative with respect to x1':  # 如果选择对 x1 的一阶偏导数
    st.latex(r'\frac{\partial{f}}{\partial{x_1}}')  # 显示数学公式
    ff = df_dx_zz  # 设置可视化数据为对 x1 的一阶偏导数

elif option_i == 'First-order partial derivative with respect to x2':  # 如果选择对 x2 的一阶偏导数
    st.latex(r'\frac{\partial{f}}{\partial{x_2}}')  # 显示数学公式
    ff = df_dy_zz  # 设置可视化数据为对 x2 的一阶偏导数

elif option_i == 'Second-order partial derivative with respect to x1':  # 如果选择对 x1 的二阶偏导数
    st.latex(r'\frac{\partial^2{f}}{\partial{x_1^2}}')  # 显示数学公式
    ff = d2f_dxdx_zz  # 设置可视化数据为对 x1 的二阶偏导数

elif option_i == 'Second-order partial derivative with respect to x2':  # 如果选择对 x2 的二阶偏导数
    st.latex(r'\frac{\partial^2{f}}{\partial{x_2^2}}')  # 显示数学公式
    ff = d2f_dydy_zz  # 设置可视化数据为对 x2 的二阶偏导数

## 使用 plotly 进行三维曲面图可视化
fig_surface = go.Figure(go.Surface(
    x=x_array,  # 设置 x 轴数据
    y=y_array,  # 设置 y 轴数据
    z=ff,  # 设置 z 轴数据为选中的偏导数值
    showscale=False,  # 不显示颜色条
    colorscale='RdYlBu_r'  # 设置颜色样式
))
fig_surface.update_layout(
    # autosize=True,  # 自动调整大小
    width=800,  # 设置图形宽度
    height=600  # 设置图形高度
)
st.plotly_chart(fig_surface)  # 在 Streamlit 中展示三维曲面图

## 使用 plotly 进行等高线图可视化
fig_contour = go.Figure(data=go.Contour(
    z=ff,  # 设置 z 轴数据为选中的偏导数值
    x=x_array,  # 设置 x 轴数据
    y=y_array,  # 设置 y 轴数据
    colorscale='RdYlBu_r'  # 设置颜色样式
))
fig_contour.update_layout(
    # autosize=True,  # 自动调整大小
    width=600,  # 设置图形宽度
    height=600  # 设置图形高度
)
st.plotly_chart(fig_contour)  # 在 Streamlit 中展示等高线图
