###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2025
###############

# 导入必要的库
import numpy as np  # 用于数值计算
import matplotlib.pyplot as plt  # 用于绘制图形
import streamlit as st  # 用于创建交互式Web应用

## 创建交互式输入界面
with st.sidebar:  # 在侧边栏添加滑块和公式显示
    
    # 显示线性函数公式
    st.latex('y = ax + b')
    
    # 创建滑块以控制斜率 a，范围为-4到4，步长为0.1
    a = st.slider('Slope, a:', 
                  min_value=-4.0, 
                  max_value=4.0, 
                  step=0.1)
    
    # 创建滑块以控制截距 b，范围为-4到4，步长为0.1
    b = st.slider('Intercept, b:', 
                  min_value=-4.0, 
                  max_value=4.0, 
                  step=0.1)

## 显示当前线性函数公式
st.latex("y = %.2f x + %.2f" % (a, b))  # 格式化显示公式

## 设置图形的全局样式
plt.rcParams["figure.figsize"] = [7.50, 3.50]  # 设置图形尺寸
plt.rcParams["figure.autolayout"] = True  # 自动调整图形布局

## 定义x和y的数据范围
x_array = np.arange(-10, 10 + 1, step=1)  # 定义x的取值范围为-10到10
y_array = a * x_array + b  # 根据公式计算y值

## 创建图形和坐标轴
fig, ax = plt.subplots()
## 设置背景透明
fig.patch.set_alpha(0)  # 设置整个图形背景为透明
ax.set_facecolor('none')  # 设置坐标轴背景为透明
# 绘制线性函数的图像
plt.plot(x_array, y_array, color='#00448A', linewidth=1.5)

# 添加坐标轴标签
plt.xlabel('$x_1$')  # 设置x轴标签
plt.ylabel('$x_2$ ')  # 设置y轴标签

# 添加x轴和y轴的零线
plt.axhline(y=0, color='0.5', linestyle='-')  # 添加y轴的零线
plt.axvline(x=0, color='0.5', linestyle='-')  # 添加x轴的零线

# 设置主刻度和次刻度
plt.xticks(np.arange(-10, 10 + 1, step=2))  # 设置主刻度
plt.yticks(np.arange(-10, 10 + 1, step=2))  # 设置主刻度
plt.axis('scaled')  # 确保坐标轴的比例一致
plt.minorticks_on()  # 开启次刻度

# 配置网格样式
ax.grid(which='major', linestyle=':', 
        linewidth='0.5', color=[0.8, 0.8, 0.8])  # 主网格样式
ax.grid(linestyle='--', linewidth=0.25, color=[0.5, 0.5, 0.5])  # 次网格样式

# 设置坐标轴范围
ax.set_xlim(-10, 10)  # 设置x轴范围
ax.set_ylim(-10, 10)  # 设置y轴范围

# 隐藏图形的边框
ax.spines['top'].set_visible(False)  # 隐藏顶部边框
ax.spines['right'].set_visible(False)  # 隐藏右侧边框
ax.spines['bottom'].set_visible(False)  # 隐藏底部边框
ax.spines['left'].set_visible(False)  # 隐藏左侧边框

## 在Streamlit中显示图形
st.pyplot(fig)  # 使用Streamlit显示图形
