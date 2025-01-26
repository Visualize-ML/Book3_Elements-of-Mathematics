###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2025
###############

# 导入必要的库
import numpy as np  # 导入numpy库，用于数值计算
from sympy import lambdify, exp, latex, symbols  # 导入sympy库，用于符号数学
import plotly.graph_objects as go  # 导入plotly的图形对象模块，用于绘制3D和等高线图
import streamlit as st  # 导入streamlit库，用于创建交互式Web应用

# 定义符号变量
x1, x2 = symbols('x1 x2')  # 定义两个符号变量x1和x2

# 定义网格参数
num = 301  # 网格点的数量
x1_array = np.linspace(-3, 3, num)  # 定义x1的取值范围，从-3到3
x2_array = np.linspace(-3, 3, num)  # 定义x2的取值范围，从-3到3
xx1, xx2 = np.meshgrid(x1_array, x2_array)  # 生成网格数据

# 定义目标函数f(x1, x2)
f_x = (3 * (1 - x1)**2 * exp(-(x1**2) - (x2 + 1)**2)  # 第一项
       - 10 * (x1 / 5 - x1**3 - x2**5) * exp(-x1**2 - x2**2)  # 第二项
       - 1 / 3 * exp(-(x1 + 1)**2 - x2**2))  # 第三项

# 将符号函数转换为数值计算函数
f_x_fcn = lambdify([x1, x2], f_x)  # 使用lambdify将符号函数转换为Python函数
f_zz = f_x_fcn(xx1, xx2)  # 计算目标函数在网格点上的值

# 在Streamlit中显示目标函数的LaTeX公式
st.latex('f(x_1, x_2) = ' + latex(f_x))  # 使用LaTeX格式显示函数公式

# ## 可视化部分
# ### 3D曲面图
fig_surface = go.Figure(go.Surface(
    x=x1_array,  # 设置x轴的取值
    y=x2_array,  # 设置y轴的取值
    z=f_zz,  # 设置z轴的取值，即函数值
    showscale=False,  # 隐藏颜色条
    colorscale='RdYlBu_r'  # 设置颜色映射为红黄蓝反转
))
fig_surface.update_layout(
    autosize=True,  # 自动调整图像大小
    width=800,  # 设置图像宽度
    height=600  # 设置图像高度
)
st.plotly_chart(fig_surface)  # 在Streamlit中显示3D曲面图

# ### 等高线图
fig_contour = go.Figure(data=go.Contour(
    z=f_zz,  # 设置z值
    x=x1_array,  # 设置x轴的取值
    y=x2_array,  # 设置y轴的取值
    colorscale='RdYlBu_r'  # 设置颜色映射为红黄蓝反转
))
fig_contour.update_layout(
    autosize=True,  # 自动调整图像大小
    width=600,  # 设置图像宽度
    height=600  # 设置图像高度
)
st.plotly_chart(fig_contour)  # 在Streamlit中显示等高线图
