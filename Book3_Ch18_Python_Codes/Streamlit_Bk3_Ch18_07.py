import numpy as np  # 导入 numpy 库，用于数值计算
import matplotlib.pyplot as plt  # 导入 matplotlib.pyplot 库，用于数据可视化
from sympy import *  # 导入 sympy 库，用于符号计算
import streamlit as st  # 导入 streamlit 库，用于创建交互式应用

## 侧边栏：设置积分区间的数量
with st.sidebar:
    # 创建滑块，用于选择积分区间数量
    num_intervals = st.slider('Number of intervals:',
                              min_value=5,  # 最小值为 5
                              max_value=50,  # 最大值为 50
                              step=1)  # 步长为 1

## 定义符号函数和积分区间
x = Symbol('x')  # 定义符号变量 x
f_x = x**2  # 定义被积函数为 f(x) = x^2

# 将符号函数转换为可执行函数
f_x_fcn = lambdify([x], f_x)

# 计算 f(x) 的不定积分
integral_f_x = integrate(f_x, x)
# 将不定积分转换为可执行函数
integral_f_x_fcn = lambdify([x], integral_f_x)

a = 0  # 积分下限
b = 1  # 积分上限

# 计算定积分的值
integral_a_b = integral_f_x_fcn(b) - integral_f_x_fcn(a)

# 使用符号库直接计算定积分
integral_a_b_v2 = integrate(f_x, (x, a, b))
integral_a_b_v2 = float(integral_a_b_v2)  # 转换为浮点数

# 打印定积分的值
print('$\\int_a^b  f(x)dx = %0.3f$' % integral_a_b)

## 可视化部分

# 计算区间宽度
delta_x = (b - a) / num_intervals

# 生成积分区间的节点
x_array = np.linspace(a, b, num_intervals + 1)
# 计算对应的函数值
y_array = f_x_fcn(x_array)

# 生成更密集的节点，用于绘制函数曲线
x_array_fine = np.linspace(a, b, 200)
y_array_fine = f_x_fcn(x_array_fine)

# 创建图形，设置大小
fig = plt.figure(figsize=(15, 5))
fig.patch.set_alpha(0)  # 设置整个图形背景为透明
## 左矩形法 Riemann 和
ax = fig.add_subplot(1, 3, 1)  # 创建子图 1
## 设置背景透明
# fig.patch.set_alpha(0)  # 设置整个图形背景为透明
ax.set_facecolor('none')  # 设置坐标轴背景为透明
# 绘制函数曲线
plt.plot(x_array_fine, y_array_fine, color='#0070C0')

# 获取左端点
x_left = x_array[:-1]
y_left = y_array[:-1]

# 绘制左端点
plt.plot(x_left, y_left, 'rx', markersize=10)

# 绘制矩形
plt.bar(x_left, y_left,
        width=delta_x,  # 矩形宽度为区间宽度
        facecolor='#DEEAF6',  # 矩形填充颜色
        align='edge',  # 矩形对齐左端点
        edgecolor='#B2B2B2')  # 矩形边框颜色

# 绘制积分上下限的垂直线
ax.axvline(x=a, color='r', linestyle='-')
ax.axvline(x=b, color='r', linestyle='-')

# 计算左矩形法的 Riemann 和
left_riemann_sum = np.sum(f_x_fcn(x_left) * delta_x)

# 设置标题
plt.title('Left Riemann sum (N = %0.0f) = %0.3f'
          % (num_intervals, left_riemann_sum))
plt.xlim((a, b))  # 设置 x 轴范围
plt.gca().spines['right'].set_visible(False)  # 隐藏右边框
plt.gca().spines['top'].set_visible(False)  # 隐藏上边框
plt.xlabel('x')  # 设置 x 轴标签
plt.ylabel('f(x)')  # 设置 y 轴标签

## 中矩形法 Riemann 和
ax = fig.add_subplot(1, 3, 2)  # 创建子图 2
## 设置背景透明

ax.set_facecolor('none')  # 设置坐标轴背景为透明
# 绘制函数曲线
plt.plot(x_array_fine, y_array_fine, color='#0070C0')

# 计算中点
x_mid = (x_array[:-1] + x_array[1:]) / 2
y_mid = f_x_fcn(x_mid)

# 绘制中点
plt.plot(x_mid, y_mid, 'rx', markersize=10)

# 绘制矩形
plt.bar(x_mid, y_mid,
        width=delta_x,
        facecolor='#DEEAF6',
        edgecolor='#B2B2B2')

# 绘制积分上下限的垂直线
ax.axvline(x=a, color='r', linestyle='-')
ax.axvline(x=b, color='r', linestyle='-')

# 计算中矩形法的 Riemann 和
mid_riemann_sum = np.sum(f_x_fcn(x_mid) * delta_x)

# 设置标题
plt.title('Middle Riemann sum (N = %0.0f) = %0.3f'
          % (num_intervals, mid_riemann_sum))
plt.xlim((a, b))
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
plt.xlabel('x')
plt.ylabel('f(x)')

## 右矩形法 Riemann 和
ax = fig.add_subplot(1, 3, 3)  # 创建子图 3
## 设置背景透明
# fig.patch.set_alpha(0)  # 设置整个图形背景为透明
ax.set_facecolor('none')  # 设置坐标轴背景为透明
# 绘制函数曲线
plt.plot(x_array_fine, y_array_fine, color='#0070C0')

# 获取右端点
x_right = x_array[1:]
y_right = y_array[1:]

# 绘制右端点
plt.plot(x_right, y_right, 'rx', markersize=10)

# 绘制矩形
plt.bar(x_right, y_right,
        width=delta_x,
        facecolor='#DEEAF6',
        align='edge',
        edgecolor='#B2B2B2')

# 绘制积分上下限的垂直线
ax.axvline(x=a, color='r', linestyle='-')
ax.axvline(x=b, color='r', linestyle='-')

# 计算右矩形法的 Riemann 和
right_riemann_sum = np.sum(f_x_fcn(x_right) * delta_x)

# 设置标题
plt.title('Right Riemann sum (N = %0.0f) = %0.3f'
          % (num_intervals, right_riemann_sum))
plt.xlim((a, b))
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
plt.xlabel('x')
plt.ylabel('f(x)')

# 在 Streamlit 中展示图形
st.pyplot(fig)
