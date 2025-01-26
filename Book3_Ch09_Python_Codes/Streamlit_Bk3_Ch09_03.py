###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2025
###############

# 导入必要的库
import streamlit as st  # 导入Streamlit库，用于创建交互式Web应用
import matplotlib.pyplot as plt  # 导入Matplotlib库，用于绘图
import numpy as np  # 导入NumPy库，用于数值计算
import matplotlib.patches as patches  # 导入Matplotlib的补丁模块，用于添加矩形

# 设置标题
st.header('Chapter 9, Dive into Conic Sections | Book 3')  # 在Streamlit页面上显示标题

## 设置侧边栏输入参数
with st.sidebar:
    # 定义m的滑动条
    m = st.slider('Define m: ', 1.0, 2.0, value=1.5, step=0.1)
    st.write('m is ' + str(m))  # 在侧边栏显示当前m的值
    
    # 定义n的滑动条
    n = st.slider('Define n: ', 1.0, 2.0, value=1.5, step=0.1)
    st.write('n is ' + str(n))  # 在侧边栏显示当前n的值

    # 定义rho的滑动条
    rho = st.slider('Define rho: ', -1.0, 1.0, value=0.0, step=0.05)
    st.write('rho is ' + str(rho))  # 在侧边栏显示当前rho的值

## 主绘图部分

# 定义网格范围和分辨率
x = np.linspace(-4, 4, num=201)  # x轴的值，从-4到4，分成201个点
y = np.linspace(-4, 4, num=201)  # y轴的值，从-4到4，分成201个点
xx, yy = np.meshgrid(x, y)  # 生成二维网格

# 创建一个绘图窗口
fig, ax = plt.subplots(figsize=(8, 8))  # 设置绘图窗口大小

# 添加矩形，用于表示椭圆的外接矩形
rect = patches.Rectangle(
    (-m, -n),  # 矩形左下角坐标
    2 * m,  # 矩形的宽度
    2 * n,  # 矩形的高度
    linewidth=0.25,  # 矩形边框的线宽
    edgecolor='0.6',  # 矩形边框的颜色
    linestyle='--',  # 矩形边框的线型
    facecolor='none'  # 矩形的填充颜色为空
)
ax.add_patch(rect)  # 将矩形添加到绘图窗口中

# 定义椭圆方程
ellipse = ((xx / m)**2 - 2 * rho * (xx / m) * (yy / n) + (yy / n)**2) / (1 - rho**2)

# 绘制椭圆的等高线
plt.contour(xx, yy, ellipse, levels=[1], colors=['b'])  # 绘制椭圆的轮廓线

# 绘制椭圆的四个顶点
plt.plot(m, rho * n, 'x', color='r', markersize=12)  # 顶点1
plt.plot(rho * m, n, 'x', color='r', markersize=12)  # 顶点2
plt.plot(-m, -rho * n, 'x', color='r', markersize=12)  # 顶点3
plt.plot(-rho * m, -n, 'x', color='r', markersize=12)  # 顶点4

# 绘制坐标轴
plt.axvline(x=0, color='0.6', linestyle='-')  # y轴
plt.axhline(y=0, color='0.6', linestyle='-')  # x轴

# 设置绘图窗口的坐标轴属性
ax.set_xticks([])  # 隐藏x轴刻度
ax.set_yticks([])  # 隐藏y轴刻度
ax.set_xlim([-2, 2])  # 设置x轴显示范围
ax.set_ylim([-2, 2])  # 设置y轴显示范围

# 隐藏绘图窗口的边框
ax.spines['top'].set_visible(False)  # 隐藏顶部边框
ax.spines['right'].set_visible(False)  # 隐藏右侧边框
ax.spines['bottom'].set_visible(False)  # 隐藏底部边框
ax.spines['left'].set_visible(False)  # 隐藏左侧边框
## 设置背景透明
fig.patch.set_alpha(0)  # 设置整个图形背景为透明
ax.set_facecolor('none')  # 设置坐标轴背景为透明
# 在Streamlit界面显示绘图
st.pyplot(fig)  # 将绘图结果嵌入到Streamlit的Web界面中
