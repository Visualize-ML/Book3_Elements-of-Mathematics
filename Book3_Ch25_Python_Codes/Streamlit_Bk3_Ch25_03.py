###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2025
###############

## 导入必要的库
import numpy as np  # 导入NumPy库，用于矩阵和数组计算
import seaborn as sns  # 导入Seaborn库，用于可视化
import matplotlib.pyplot as plt  # 导入Matplotlib库，用于绘图
import streamlit as st  # 导入Streamlit库，用于交互式展示

## 定义绘制向量的函数
def draw_vector(vector, RBG, ax):  # 自定义函数，用于绘制二维向量
    ax.quiver(0, 0, vector[0], vector[1],  # 绘制从原点到指定点的向量
              angles='xy',  # 设置为笛卡尔坐标系
              scale_units='xy',  # 使用笛卡尔单位
              scale=1,  # 设置比例为1，表示实际大小
              color=RBG)  # 设置向量颜色

## 定义转移矩阵
T = np.matrix([[0.7, 0.2],  # 定义转移矩阵T，第一行表示从状态1到状态1和状态2的转移概率
               [0.3, 0.8]])  # 第二行表示从状态2到状态1和状态2的转移概率

## 定义LaTeX格式化函数
def bmatrix(a):  # 自定义函数，用于将矩阵转换为LaTeX的bmatrix格式
    if len(a.shape) > 2:  # 检查矩阵的维度是否大于2
        raise ValueError('bmatrix can at most display two dimensions')  # 如果维度大于2，抛出错误
    lines = str(a).replace('[', '').replace(']', '').splitlines()  # 将矩阵转为字符串并分行处理
    rv = [r'\begin{bmatrix}']  # 添加LaTeX起始语法
    rv += ['  ' + ' & '.join(l.split()) + r'\\' for l in lines]  # 按行拼接LaTeX矩阵格式
    rv += [r'\end{bmatrix}']  # 添加LaTeX结束语法
    return '\n'.join(rv)  # 返回拼接后的字符串

## 定义初始状态向量和交互式组件
with st.sidebar:  # 创建Streamlit侧边栏
    p = st.slider('Ratio of chickens: ',  # 滑块，用于选择鸡的初始比例
                  min_value=0.0,  # 最小值为0
                  max_value=1.0,  # 最大值为1
                  step=0.05)  # 步长为0.05

    num_steps = st.slider('Number of nights: ',  # 滑块，用于选择时间步数
                          min_value=10,  # 最小值为10
                          max_value=20,  # 最大值为20
                          step=1)  # 步长为1

    pi_0 = np.array([[p],  # 根据选择的鸡的比例计算初始状态向量
                     [1-p]])  # 兔的比例为1减去鸡的比例

    st.latex('T = ' + bmatrix(T))  # 显示转移矩阵T的LaTeX格式
    st.latex('\pi (0) = ' + bmatrix(pi_0))  # 显示初始状态向量的LaTeX格式
    st.latex('\pi(k + 1) = T \pi(k)')  # 显示状态转移公式的LaTeX格式

## 创建单位圆的网格和模长计算
x1 = np.linspace(-1.1, 1.1, num=201)  # 定义x轴的取值范围
x2 = x1  # 定义y轴的取值范围，与x轴相同
xx1, xx2 = np.meshgrid(x1, x2)  # 生成二维网格
zz = ((np.abs((xx1))**2) + (np.abs((xx2))**2))**(1./2)  # 计算网格中每点的模长

## 初始化状态向量
pi = pi_0  # 设置初始状态向量为用户选择的初始值

## 定义颜色渐变
colors = plt.cm.rainbow(np.linspace(0, 1, num_steps + 1))  # 为每个时间步生成颜色

## 创建图形
fig, ax = plt.subplots(figsize=(10, 10))  # 创建图形和坐标轴

## 设置背景透明
fig.patch.set_alpha(0)  # 设置整个图形背景为透明
ax.set_facecolor('none')  # 设置坐标轴背景为透明

## 绘制参考线
plt.plot(x1, 1 - x1, color='k',  # 绘制参考线y=1-x
         linestyle='--')  # 设置参考线为虚线

## 绘制单位圆
plt.contour(xx1, xx2, zz, levels=[1],  # 绘制模长为1的等高线，即单位圆
            colors='0.5', linestyles=['--'])  # 设置颜色为黑色，线型为虚线

## 遍历时间步并绘制状态向量
for i in np.arange(0, num_steps + 1):  # 遍历每个时间步
    draw_vector(pi / np.linalg.norm(pi), colors[i], ax)  # 绘制归一化状态向量
    draw_vector(pi, colors[i], ax)  # 绘制原始状态向量
    pi = T @ pi  # 更新状态向量，使用转移矩阵进行计算

## 设置图形样式
ax.tick_params(left=False, bottom=False)  # 隐藏坐标轴刻度线
ax.set_xlim(-1.1, 1.1)  # 设置x轴范围
ax.set_ylim(-1.1, 1.1)  # 设置y轴范围
ax.axvline(x=0, color='0.5')  # 绘制y轴
ax.axhline(y=0, color='0.5')  # 绘制x轴
ax.spines['top'].set_visible(False)  # 隐藏上边框
ax.spines['right'].set_visible(False)  # 隐藏右边框
ax.spines['bottom'].set_visible(False)  # 隐藏下边框
ax.spines['left'].set_visible(False)  # 隐藏左边框
ax.grid(color=[0.8, 0.8, 0.8])  # 设置网格颜色
plt.xticks(np.linspace(-1, 1, 21))  # 设置x轴刻度
plt.yticks(np.linspace(-1, 1, 21))  # 设置y轴刻度

## 显示图形
st.pyplot(fig=fig)  # 使用Streamlit显示图形
