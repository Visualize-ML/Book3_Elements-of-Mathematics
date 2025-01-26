###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2025
###############

## 导入必要的库
import numpy as np  # 导入NumPy库，用于数值计算
import streamlit as st  # 导入Streamlit库，用于交互式展示
import plotly.express as px  # 导入Plotly Express库，用于绘制交互式图表
import pandas as pd  # 导入Pandas库，用于数据处理
import plotly.graph_objects as go  # 导入Plotly图形对象库，用于添加自定义图层

## 定义鸡和兔的数据
num_chickens = np.array([32, 110, 71, 79, 45, 20, 56, 55, 87, 68, 87, 63, 31, 88])  # 鸡的数量数据
num_rabbits = np.array([22, 53, 39, 40, 25, 15, 34, 34, 52, 41, 43, 33, 24, 52])  # 兔的数量数据

## 创建一个DataFrame，用于可视化
df = pd.DataFrame(np.vstack((num_chickens, num_rabbits)).T,  # 将鸡和兔的数据堆叠并转置
                  columns=['num_chickens', 'num_rabbits'])  # 设置列名为鸡的数量和兔的数量

## 在侧边栏设置交互式参数
with st.sidebar:  # 创建侧边栏
    st.latex('\hat{y} = ax + b')  # 显示线性回归公式
    a = st.slider('a, slope:',  # 滑块，用于选择斜率a
                  min_value=0.05,  # 设置斜率的最小值为0.05
                  max_value=1.0,  # 设置斜率的最大值为1.0
                  step=0.01)  # 每次调整的步长为0.01
    b = st.slider('b, intercept:',  # 滑块，用于选择截距b
                  min_value=0.0,  # 设置截距的最小值为0.0
                  max_value=10.0,  # 设置截距的最大值为10.0
                  step=0.1)  # 每次调整的步长为0.1

## 计算预测值和误差
y_hat = a * num_chickens + b  # 根据选定的斜率和截距计算预测值
SSE = np.sum((num_rabbits - y_hat) ** 2)  # 计算平方误差的总和

## 在Streamlit中显示误差
st.write('Sum of squared errors (SSE): %.2f' % SSE)  # 在页面显示平方误差

## 绘制散点图和回归线
fig = px.scatter(df, x="num_chickens", y="num_rabbits", trendline="ols")  # 使用Plotly绘制散点图和OLS回归线

## 添加预测值的自定义图层
fig.add_trace(go.Scatter(x=num_chickens, y=y_hat,  # 添加预测值的散点
                         name='Predicted',  # 设置图例名称
                         line=dict(color='red', width=1)))  # 设置预测线的颜色和宽度

## 在Streamlit中展示图形
st.plotly_chart(fig)  # 将绘制的图形嵌入到Streamlit页面
