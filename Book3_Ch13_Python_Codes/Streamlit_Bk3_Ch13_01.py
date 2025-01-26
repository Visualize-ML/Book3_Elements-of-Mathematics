###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2025
###############

import math  # 导入数学模块
import numpy as np  # 导入 numpy 模块，用于数值计算
import matplotlib.pyplot as plt  # 导入 matplotlib 模块，用于绘图
from matplotlib import cm  # 导入 matplotlib 的 colormap，用于颜色映射
import streamlit as st  # 导入 streamlit 模块，用于创建交互式界面
from sympy import symbols, lambdify  # 导入 sympy 模块，用于符号运算
import plotly.graph_objects as go  # 导入 plotly 的 graph_objects，用于交互式绘图

## 定义生成网格的函数
def mesh_square(x1_0, x2_0, r, num):
    rr = np.linspace(-r, r, num)  # 在指定范围生成均匀分布的点
    xx1, xx2 = np.meshgrid(rr, rr)  # 创建二维网格
    xx1 = xx1 + x1_0  # 平移网格中心到 x1_0
    xx2 = xx2 + x2_0  # 平移网格中心到 x2_0
    return xx1, xx2, rr  # 返回生成的网格和坐标数组

## 定义绘制 3D 曲面的函数
def plot_surf(xx1, xx2, ff):
    norm_plt = plt.Normalize(ff.min(), ff.max())  # 归一化颜色映射范围
    colors = cm.coolwarm(norm_plt(ff))  # 使用 coolwarm 颜色映射
    fig = plt.figure()  # 创建图形
    ax = fig.add_subplot(projection='3d')  # 添加 3D 坐标轴
    surf = ax.plot_surface(xx1, xx2, ff, facecolors=colors, shade=False)  # 绘制曲面
    surf.set_facecolor((0, 0, 0, 0))  # 设置背景为透明
    ax.set_xlabel('$\it{x_1}$')  # 设置 x 轴标签
    ax.set_ylabel('$\it{x_2}$')  # 设置 y 轴标签
    ax.set_zlabel('$\it{f}$($\it{x_1}$,$\it{x_2}$)')  # 设置 z 轴标签
    return fig  # 返回绘制的图形

## 定义绘制等高线的函数
def plot_contourf(xx1, xx2, ff):
    fig, ax = plt.subplots()  # 创建图形和坐标轴
    cntr2 = ax.contourf(xx1, xx2, ff, levels=15, cmap="RdBu_r")  # 绘制填充等高线
    fig.colorbar(cntr2, ax=ax)  # 添加颜色条
    ax.set_xlabel('$\it{x_1}$')  # 设置 x 轴标签
    ax.set_ylabel('$\it{x_2}$')  # 设置 y 轴标签
    ax.grid(linestyle='--', linewidth=0.25, color=[0.5, 0.5, 0.5])  # 设置网格样式
    return fig  # 返回绘制的图形

## 设置 Streamlit 侧边栏交互控件
with st.sidebar:
    st.latex(r'f(x_1,x_2) = ax_1^2 + bx_1x_2 + cx_2^2 + dx_1 + ex_2 + f')  # 显示数学公式
    a = st.slider('a', min_value=-2.0, max_value=2.0, step=0.1)  # 滑动条选择参数 a
    b = st.slider('b', min_value=-2.0, max_value=2.0, step=0.1)  # 滑动条选择参数 b
    c = st.slider('c', min_value=-2.0, max_value=2.0, step=0.1)  # 滑动条选择参数 c
    d = st.slider('d', min_value=-2.0, max_value=2.0, step=0.1)  # 滑动条选择参数 d
    e = st.slider('e', min_value=-2.0, max_value=2.0, step=0.1)  # 滑动条选择参数 e
    f = st.slider('f', min_value=-2.0, max_value=2.0, step=0.1)  # 滑动条选择参数 f

## 初始化网格和符号表达式
x1, x2 = symbols('x1 x2')  # 定义符号变量
x1_0, x2_0 = 0, 0  # 设置网格中心
r, num = 2, 30  # 设置网格半径和点数
xx1, xx2, x1_array = mesh_square(x1_0, x2_0, r, num)  # 生成网格
x2_array = x1_array  # y 轴坐标与 x 轴一致

## 使用 matplotlib 可视化
f_sym = a * x1**2 + b * x1 * x2 + c * x2**2 + d * x1 + e * x2 + f  # 定义目标函数
f_fcn = lambdify([x1, x2], f_sym)  # 将符号函数转换为数值函数
ff = f_fcn(xx1, xx2)  # 计算目标函数值
fig_1 = plot_surf(xx1, xx2, ff)  # 绘制 3D 曲面
fig_2 = plot_contourf(xx1, xx2, ff)  # 绘制等高线

## 使用 Plotly 可视化
fig_surface = go.Figure(go.Surface(
    x=x1_array, y=x2_array, z=ff, showscale=False, colorscale='RdYlBu_r'))  # 绘制交互式 3D 曲面
fig_surface.update_layout(autosize=True, width=800, height=600)  # 设置布局大小
st.plotly_chart(fig_surface)  # 在 Streamlit 中显示 3D 曲面图

fig_contour = go.Figure(data=go.Contour(
    z=ff, x=x1_array, y=x2_array, colorscale='RdYlBu_r'))  # 绘制交互式等高线
fig_contour.update_layout(autosize=True, width=600, height=600)  # 设置布局大小
st.plotly_chart(fig_contour)  # 在 Streamlit 中显示等高线图
