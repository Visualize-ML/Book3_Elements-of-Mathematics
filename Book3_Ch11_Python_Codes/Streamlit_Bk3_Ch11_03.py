import streamlit as st  # 导入Streamlit库，用于创建Web应用
import numpy as np  # 导入numpy库，用于数值计算
import plotly.graph_objects as go  # 导入plotly的图形对象模块

# 定义x的取值范围
x = np.linspace(-2, 2, 100)  # x轴从-2到2，分成100个点

# 定义一次、二次、三次函数
linear = x  # 一次函数 f1(x) = x
quadratic = x**2  # 二次函数 f2(x) = x^2
cubic = x**3  # 三次函数 f3(x) = x^3

# 定义绘图函数
def plot_curve(x, y, title="Function Plot"):
    """
    使用Plotly绘制曲线
    """
    fig = go.Figure()  # 创建一个Plotly图形对象
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name=title, line=dict(width=2)))  # 添加曲线

    # 配置布局
    fig.update_layout(
        title=title,
        xaxis_title="x",
        yaxis_title="f(x)",
        xaxis=dict(showgrid=True, zeroline=True),
        yaxis=dict(showgrid=True, zeroline=True),
        template="plotly_white",
        legend=dict(x=0.02, y=0.98),
    )
    # 显示图形
    st.plotly_chart(fig)

# Streamlit 应用布局
st.title("单项式叠加函数展示")  # 设置应用标题
st.write("### 基本函数图像")  # 设置小标题

# 绘制一次、二次、三次函数图像
st.write("**一次函数**: $f_1(x) = x$")
plot_curve(x, linear, title="f1(x) = x")

st.write("**二次函数**: $f_2(x) = x^2$")
plot_curve(x, quadratic, title="f2(x) = x^2")

st.write("**三次函数**: $f_3(x) = x^3$")
plot_curve(x, cubic, title="f3(x) = x^3")

# 用户交互选择
st.write("### 叠加函数设置")
st.write("请选择叠加系数 $a$, $b$, $c$ 对应的权重:")

# 使用多选按钮获取用户选择
selected_terms = st.multiselect(
    "选择要叠加的单项式：",
    ["一次函数 ($f_1(x) = x$)", "二次函数 ($f_2(x) = x^2$)", "三次函数 ($f_3(x) = x^3$)"],
    default=["一次函数 ($f_1(x) = x$)"]
)

# 定义初始系数
a, b, c = 0, 0, 0
if "一次函数 ($f_1(x) = x$)" in selected_terms:
    a = st.slider("设置 $a$ 的值:", -10.0, 10.0, 1.0, step=0.1)
if "二次函数 ($f_2(x) = x^2$)" in selected_terms:
    b = st.slider("设置 $b$ 的值:", -10.0, 10.0, 1.0, step=0.1)
if "三次函数 ($f_3(x) = x^3$)" in selected_terms:
    c = st.slider("设置 $c$ 的值:", -10.0, 10.0, 1.0, step=0.1)

# 叠加函数计算
combined_function = a * linear + b * quadratic + c * cubic

# 显示叠加函数公式
st.write("### 叠加函数公式")
latex_formula = f"f(x) = {a:.2f} \\cdot x + {b:.2f} \\cdot x^2 + {c:.2f} \\cdot x^3"
st.latex(latex_formula)

# 绘制叠加函数图像
st.write("### 叠加函数图像")
plot_curve(x, combined_function, title="叠加函数 f(x)")
