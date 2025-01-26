###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2025
###############

# 导入所需的库
import streamlit as st  # 导入 Streamlit，用于创建交互式 Web 应用
import matplotlib.pyplot as plt  # 导入 Matplotlib，用于绘制图形
from matplotlib.patches import RegularPolygon, Circle  # 导入 RegularPolygon 和 Circle，用于绘制多边形和圆
import numpy as np  # 导入 NumPy，用于数值计算

# == 第一部分：设置边数的交互滑块 ==
with st.sidebar:
    # 创建滑块，用于用户选择多边形的边数
    num_vertices = st.slider(
        'Number of sides of polygon：',  # 滑块的描述
        min_value=4,  # 滑块的最小值
        max_value=20,  # 滑块的最大值
        step=1  # 滑块的步长
    )
    
# == 第二部分：绘制多边形和内接圆、外接圆 ==
fig_1, ax = plt.subplots()  # 创建一个 Matplotlib 图形对象和坐标轴对象
ax.set_aspect('equal')  # 设置坐标轴比例相等
## 设置背景透明
fig_1.patch.set_alpha(0)  # 设置整个图形背景为透明
ax.set_facecolor('none')  # 设置坐标轴背景为透明
# 绘制内接多边形
hexagon_inner = RegularPolygon(
    (0, 0),  # 多边形的中心坐标
    numVertices=num_vertices,  # 多边形的边数
    radius=1,  # 多边形的半径
    alpha=0.2,  # 透明度
    edgecolor='0.6'  # 边框颜色
)
ax.add_patch(hexagon_inner)  # 将内接多边形添加到坐标轴

# 绘制外接多边形
hexagon_outer = RegularPolygon(
    (0, 0),  # 多边形的中心坐标
    numVertices=num_vertices,  # 多边形的边数
    radius=1 / np.cos(np.pi / num_vertices),  # 外接多边形的半径
    alpha=0.2,  # 透明度
    edgecolor='0.6'  # 边框颜色
)
ax.add_patch(hexagon_outer)  # 将外接多边形添加到坐标轴

# 绘制圆
circle = Circle(
    (0, 0),  # 圆心坐标
    radius=1,  # 圆的半径
    facecolor='none',  # 圆的填充颜色
    edgecolor='0.6'  # 圆的边框颜色
)
ax.add_patch(circle)  # 将圆添加到坐标轴

# 关闭坐标轴
plt.axis('off')

# 设置显示范围
plt.xlim(-1.5, 1.5)  # x 轴范围
plt.ylim(-1.5, 1.5)  # y 轴范围
plt.show()  # 显示图形

# 在 Streamlit 界面中显示图形
st.pyplot(fig_1)

# == 第三部分：通过内接和外接多边形估算圆周率 ==
# 创建多边形边数的数组
n_array = np.linspace(3, num_vertices)

# 计算内接多边形和外接多边形估算的 π 的上下界
pi_lower_b = np.sin(np.pi / n_array) * n_array  # 内接多边形的估算
pi_upper_b = np.tan(np.pi / n_array) * n_array  # 外接多边形的估算

# 创建一个新图形对象用于绘制 π 的估算范围
fig_2, ax = plt.subplots()
## 设置背景透明
fig_2.patch.set_alpha(0)  # 设置整个图形背景为透明
ax.set_facecolor('none')  # 设置坐标轴背景为透明
# 添加实际的 π 作为参考线
plt.axhline(y=np.pi, color='r', linestyle='-')

# 绘制内接多边形和外接多边形的 π 的估算曲线
plt.plot(n_array, pi_lower_b, color='b', label='Lower Bound')  # 内接多边形估算曲线
plt.plot(n_array, pi_upper_b, color='g', label='Upper Bound')  # 外接多边形估算曲线

# 填充 π 的估算范围
plt.fill_between(n_array, pi_lower_b, pi_upper_b, color='#DEEAF6', label='Estimate Range')

# 设置布局和标签
plt.tight_layout()  # 自动调整子图布局
plt.xlabel('Number of sides, n')  # x 轴标签
plt.ylabel('Estimate of $\pi$')  # y 轴标签

# 设置 x 轴的范围
plt.xlim((n_array.min(), n_array.max()))

# 在 Streamlit 界面中显示图形
st.pyplot(fig_2)
