###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2025
###############

# 导入必要的库
import numpy as np  # 用于生成随机矩阵并进行矩阵运算
import streamlit as st  # 用于创建交互式Web应用
import seaborn as sns  # 用于绘制热力图
from matplotlib import pyplot as plt  # 用于生成图形

# 定义函数bmatrix，将二维数组转换为LaTeX格式的矩阵
def bmatrix(a):
    """
    将NumPy数组转换为LaTeX bmatrix格式的字符串表示
    :param a: 输入的NumPy数组
    :return: LaTeX格式的bmatrix字符串
    """
    if len(a.shape) > 2:  # 确保输入是二维数组
        raise ValueError('bmatrix can at most display two dimensions')  # 超过二维时报错
    lines = str(a).replace('[', '').replace(']', '').splitlines()  # 去掉中括号并分行
    rv = [r'\begin{bmatrix}']  # 起始LaTeX矩阵标记
    rv += ['  ' + ' & '.join(l.split()) + r'\\' for l in lines]  # 按行拼接元素
    rv += [r'\end{bmatrix}']  # 结束LaTeX矩阵标记
    return '\n'.join(rv)  # 返回完整的LaTeX bmatrix字符串

# 在侧边栏添加用户交互控件
with st.sidebar:
    st.latex(r'C_{m\times n} = A_{m\times p} B_{p\times n}')  # 显示矩阵乘法公式
    # 用户选择矩阵A的行数
    rows_A = st.slider('Number of rows in A:',
                       min_value=1,
                       max_value=9,
                       value=5,
                       step=1)
    # 用户选择矩阵A的列数
    cols_A = st.slider('Number of columns in A:',
                       min_value=1,
                       max_value=9,
                       value=5,
                       step=1)
    # 用户选择矩阵B的行数
    rows_B = st.slider('Number of rows in B:',
                       min_value=1,
                       max_value=9,
                       value=5,
                       step=1)
    # 用户选择矩阵B的列数
    cols_B = st.slider('Number of columns in B:',
                       min_value=1,
                       max_value=9,
                       value=5,
                       step=1)

# 生成随机矩阵A和B
A = np.random.randint(10, size=(rows_A, cols_A))  # 随机生成0到9的整数矩阵A
B = np.random.randint(10, size=(rows_B, cols_B))  # 随机生成0到9的整数矩阵B

# 在界面显示矩阵A和B的LaTeX格式
st.latex(r'A_{m\times p} = ' + bmatrix(A))  # 显示矩阵A
st.latex(r'B_{p\times n} = ' + bmatrix(B))  # 显示矩阵B

# 尝试执行矩阵乘法
try:
    # 计算矩阵C = A * B
    C = A @ B
    st.latex('C = AB = ' + bmatrix(C))  # 显示矩阵C的LaTeX格式
    
    # 创建子图，显示矩阵热力图
    fig, axs = plt.subplots(1, 5, figsize=(12, 3))
    ## 设置背景透明
    fig.patch.set_alpha(0)  # 设置整个图形背景为透明
    
    # 绘制矩阵A的热力图
    plt.sca(axs[0])
    ax = sns.heatmap(A, cmap='RdYlBu_r',
                     cbar_kws={"orientation": "horizontal"},
                     yticklabels=np.arange(1, rows_A + 1),
                     xticklabels=np.arange(1, cols_A + 1))
    ax.set_aspect("equal")  # 保持比例
    ax.set_facecolor('none')  # 设置坐标轴背景为透明
    plt.title('$A$')  # 设置标题
    plt.yticks(rotation=0)
    
    # 显示矩阵乘法符号
    plt.sca(axs[1])
    plt.title('$@$')  # 矩阵乘法符号
    plt.axis('off')
    
    # 绘制矩阵B的热力图
    plt.sca(axs[2])
    ax = sns.heatmap(B, cmap='RdYlBu_r',
                     cbar_kws={"orientation": "horizontal"},
                     yticklabels=np.arange(1, rows_B + 1),
                     xticklabels=np.arange(1, cols_B + 1))
    ax.set_aspect("equal")
    ax.set_facecolor('none')  # 设置坐标轴背景为透明
    plt.title('$B$')
    plt.yticks(rotation=0)
    
    # 显示等号
    plt.sca(axs[3])
    plt.title('$=$')  # 等号
    plt.axis('off')
    
    # 绘制矩阵C的热力图
    plt.sca(axs[4])
    ax = sns.heatmap(C, cmap='RdYlBu_r',
                     cbar_kws={"orientation": "horizontal"},
                     yticklabels=np.arange(1, rows_A + 1),
                     xticklabels=np.arange(1, cols_B + 1))
    ax.set_aspect("equal")
    ax.set_facecolor('none')  # 设置坐标轴背景为透明
    plt.title('$C$')
    plt.yticks(rotation=0)
    
    # 在界面显示热力图
    st.pyplot(fig)
    
except:  # 如果矩阵乘法无法进行（列数不等于行数），提示用户
    st.write('The number of columns of the first matrix, must equal the number of rows of the second matrix.')
