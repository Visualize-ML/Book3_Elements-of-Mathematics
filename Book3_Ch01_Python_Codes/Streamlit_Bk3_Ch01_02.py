###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2025
###############

# 导入必要的库
from mpmath import mp  # 用于高精度计算
import streamlit as st  # 用于创建交互式Web应用
import numpy as np  # 用于数值计算
import matplotlib.pyplot as plt  # 用于绘制图形

# 添加Streamlit侧边栏用户输入
with st.sidebar:
    # 用户选择小数位数
    num_digits = st.slider('Number of decimal digits:',  # 滑块标题
                           min_value=10000,  # 最小值为10,000
                           max_value=100000,  # 最大值为100,000
                           step=10000)  # 每次增加的步长为10,000

# 设置mpmath的计算精度为用户选择的位数加2（额外位数用于内部计算）
mp.dps = num_digits + 2

# 获取π的高精度小数部分
pi_digits = mp.pi  # 计算π的高精度值
pi_digits = str(pi_digits)[2:]  # 转换为字符串并去掉小数点前的部分

# 将小数部分的每一位转换为整数列表
pi_digits_list = [int(x) for x in pi_digits]

# 将整数列表转换为NumPy数组
pi_digits_array = np.array(pi_digits_list)

# 统计每个数字（0-9）的出现次数
counts = np.bincount(pi_digits_array)

# 创建一个水平条形图来显示数字的出现次数
fig, ax = plt.subplots()  # 创建图形和子图
## 设置背景透明
fig.patch.set_alpha(0)  # 设置整个图形背景为透明
ax.set_facecolor('none')  # 设置坐标轴背景为透明
# 绘制水平条形图
ax.barh(range(10), counts, align='center',
        edgecolor=[0.6, 0.6, 0.6])  # 灰色边框

# 去掉顶部和右侧的坐标轴边框
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# 添加x轴和y轴标签
ax.set_xlabel('Count')  # x轴标签
ax.set_ylabel('Digit, 0~9')  # y轴标签

# 设置y轴刻度标签为数字0到9
plt.yticks(range(10))

# 在Streamlit应用中显示绘制的图形
st.pyplot(fig)
