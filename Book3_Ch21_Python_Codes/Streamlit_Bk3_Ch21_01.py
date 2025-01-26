###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2025
###############

## 导入必要的库
import streamlit as st  # 导入Streamlit库，用于创建交互式Web应用
import plotly.express as px  # 导入Plotly库中的express模块，用于数据可视化

## 加载鸢尾花数据集
df = px.data.iris()  # 使用Plotly内置的函数加载鸢尾花数据集

## 从数据集中提取特征列名
features = df.columns.to_list()[:-2]  # 获取数据集的前四列作为特征名称列表

## 在侧边栏中创建交互式控件
with st.sidebar:  # 创建Streamlit的侧边栏
    st.write('2D scatter plot')  # 显示侧边栏的标题

    x_feature = st.radio('Horizontal axis',  # 创建单选按钮选择水平轴的特征
                         features)

    y_feature = st.radio('Vertical axis',  # 创建单选按钮选择垂直轴的特征
                         features)

    marginal_x = st.radio('Horizontal marginal',  # 创建单选按钮选择水平轴的边际分布类型
                          ["histogram", 
                           "rug", 
                           "box", 
                           "violin"])

    marginal_y = st.radio('Vertical marginal',  # 创建单选按钮选择垂直轴的边际分布类型
                          ["histogram", 
                           "rug", 
                           "box", 
                           "violin"])

## 展示原始数据部分
with st.expander('Original data'):  # 创建一个可折叠部分，标题为"Original data"
    st.write(df)  # 在可折叠部分中显示鸢尾花数据集

## 绘制二维散点图部分
with st.expander('2D scatter plot'):  # 创建一个可折叠部分，标题为"2D scatter plot"

    fig_2 = px.scatter(df,  # 使用Plotly的散点图绘制函数
                       x=x_feature,  # 设置x轴的特征
                       y=y_feature,  # 设置y轴的特征
                       color="species",  # 根据物种类别进行颜色分组
                       marginal_x=marginal_x,  # 设置水平边际分布类型
                       marginal_y=marginal_y)  # 设置垂直边际分布类型

    st.plotly_chart(fig_2)  # 在Streamlit应用中显示生成的散点图
