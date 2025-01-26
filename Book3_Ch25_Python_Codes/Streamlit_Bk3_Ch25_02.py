###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2025
###############

## 导入必要的库
import numpy as np  # 导入NumPy库，用于矩阵计算
import streamlit as st  # 导入Streamlit库，用于交互式展示
import plotly.express as px  # 导入Plotly库，用于创建交互式图表

## 定义将矩阵转换为LaTeX格式的函数
def bmatrix(a):  # 自定义函数，用于生成LaTeX格式的bmatrix
    if len(a.shape) > 2:  # 检查输入矩阵是否超过二维
        raise ValueError('bmatrix can at most display two dimensions')  # 抛出错误提示
    lines = str(a).replace('[', '').replace(']', '').splitlines()  # 将矩阵转换为字符串并按行分割
    rv = [r'\begin{bmatrix}']  # 添加LaTeX起始语法
    rv += ['  ' + ' & '.join(l.split()) + r'\\' for l in lines]  # 按行格式化为LaTeX矩阵格式
    rv += [r'\end{bmatrix}']  # 添加LaTeX结束语法
    return '\n'.join(rv)  # 返回拼接后的字符串

## 定义转移矩阵T
T = np.matrix([[0.7, 0.2],  # 第一行表示从状态1到状态1和状态2的转移概率
               [0.3, 0.8]])  # 第二行表示从状态2到状态1和状态2的转移概率

## 在侧边栏设置交互式组件
with st.sidebar:  # 创建Streamlit侧边栏
    p = st.slider('Ratio of chickens: ',  # 滑块，用于选择初始鸡的比例
                  min_value=0.0,  # 最小值为0
                  max_value=1.0,  # 最大值为1
                  step=0.05)  # 每次变化的步长为0.05

    num_steps = st.slider('Number of nights: ',  # 滑块，用于选择时间步数
                          min_value=10,  # 最小值为10
                          max_value=30,  # 最大值为30
                          step=1)  # 每次变化的步长为1

    pi_0 = np.array([[p],  # 根据选择的鸡的比例生成初始状态向量
                     [1-p]])  # 兔的比例为1减去鸡的比例

    st.latex('T = ' + bmatrix(T))  # 在侧边栏显示转移矩阵的LaTeX格式
    st.latex('\pi (0) = ' + bmatrix(pi_0))  # 显示初始状态向量的LaTeX格式
    st.latex('\pi(k + 1) = T \pi(k)')  # 显示状态转移公式的LaTeX格式

## 初始化状态向量数组
pi_array = pi_0  # 初始化状态向量数组为初始状态向量
pi_idx = pi_0  # 设置当前状态向量为初始状态向量

## 计算多个时间步的状态转移
for idx in np.arange(0, num_steps):  # 遍历每个时间步
    pi_idx = T @ pi_idx  # 使用转移矩阵更新当前状态向量
    pi_array = np.column_stack((pi_array, pi_idx))  # 将当前状态向量添加到状态向量数组中

## 可视化状态向量的转移
fig = px.imshow(pi_array, text_auto=True,  # 使用Plotly生成状态向量的热力图
                color_continuous_scale='RdYlBu_r')  # 设置颜色映射为红-黄-蓝渐变

fig.update_layout(  # 更新图表布局
    autosize=False,  # 禁用自动调整大小
    width=1000,  # 设置图表宽度为1000
    height=500,  # 设置图表高度为500
    coloraxis_showscale=False)  # 隐藏颜色条

st.plotly_chart(fig)  # 在Streamlit中显示图表
