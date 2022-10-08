
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############


import streamlit as st
import plotly.express as px

# load iris data
df = px.data.iris()

features = df.columns.to_list()[:-2]
with st.sidebar:
    st.write('2D scatter plot')
    x_feature = st.radio('Horizontal axis',
             features)
    y_feature = st.radio('Vertical axis',
             features)
    
    marginal_x = st.radio('Horizontal marginal',
                          ["histogram", 
                           "rug", 
                           "box", 
                           "violin"])
    
    marginal_y = st.radio('Vertical marginal',
                          ["histogram", 
                           "rug", 
                           "box", 
                           "violin"])


#%% original data

with st.expander('Original data'):
    st.write(df)
    

#%% 2D scatter plot
with st.expander('2D scatter plot'):

    fig_2 = px.scatter(df, x=x_feature, y=y_feature, color="species",
                     marginal_x=marginal_x, marginal_y=marginal_y)

    st.plotly_chart(fig_2)


    
