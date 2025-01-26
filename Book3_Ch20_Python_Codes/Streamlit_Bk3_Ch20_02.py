import numpy as np
import plotly.graph_objects as go
import streamlit as st

# 在 Streamlit 侧边栏设置参数
with st.sidebar:
    num_toss = st.slider('Number of toss:',
                         min_value=50,
                         max_value=200,
                         step=1)  # 设置抛硬币次数
    rnd_seed = st.slider('Random seed number',
                         min_value=0,
                         max_value=100,
                         step=1)  # 设置随机种子

# 设置随机种子
np.random.seed(rnd_seed)

# 生成抛硬币结果（0 表示正面，1 表示反面）
toss = np.random.randint(low=0, high=2, size=(num_toss, 1))

# 计算每次抛硬币的累积均值
iteration = np.arange(1, num_toss + 1)  # 生成迭代序列
cum_mean = np.cumsum(toss) / iteration  # 计算累积均值

# 创建第一幅图：抛硬币的散点图
scatter_fig = go.Figure()

# 添加正面的散点
scatter_fig.add_trace(go.Scatter(
    x=iteration[toss.flatten() == 1],
    y=toss[toss == 1].flatten(),
    mode='markers',
    marker=dict(color='red', size=6),
    name='Head (1)'
))

# 添加反面的散点
scatter_fig.add_trace(go.Scatter(
    x=iteration[toss.flatten() == 0],
    y=toss[toss == 0].flatten(),
    mode='markers',
    marker=dict(color='blue', size=6),
    name='Tail (0)'
))

# 设置图表布局
scatter_fig.update_layout(
    title='Coin Toss Results',
    xaxis_title='Iteration',
    yaxis_title='Result (0: Tail, 1: Head)',
    yaxis=dict(tickvals=[0, 1]),
    showlegend=True
)

# 创建第二幅图：累积均值折线图
mean_fig = go.Figure()

# 添加累积均值曲线
mean_fig.add_trace(go.Scatter(
    x=iteration,
    y=cum_mean,
    mode='lines',
    line=dict(color='green'),
    name='Cumulative Mean'
))

# 添加水平线 y=0.5
mean_fig.add_trace(go.Scatter(
    x=[1, num_toss],
    y=[0.5, 0.5],
    mode='lines',
    line=dict(color='red', dash='dash'),
    name='Mean = 0.5'
))

# 设置图表布局
mean_fig.update_layout(
    title='Cumulative Mean of Coin Toss',
    xaxis_title='Iteration',
    yaxis_title='Cumulative Mean',
    yaxis=dict(tickvals=[0, 0.5, 1]),
    showlegend=True
)

# 在 Streamlit 中展示图表
st.plotly_chart(scatter_fig)  # 显示抛硬币结果图
st.plotly_chart(mean_fig)  # 显示累积均值图
