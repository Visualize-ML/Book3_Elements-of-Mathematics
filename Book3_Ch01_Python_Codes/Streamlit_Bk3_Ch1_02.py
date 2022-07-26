
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Streamlit_Bk3_Ch1_02.py

from mpmath import mp
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

with st.sidebar:
    

    num_digits = st.slider('Number of decimal digits:',
                           min_value = 10000, 
                           max_value = 100000,
                           step = 10000)
    
mp.dps = num_digits + 2
pi_digits = mp.pi
# st.write(str(pi_digits))
pi_digits = str(pi_digits)[2:]
pi_digits_list = [int(x) for x in pi_digits]
# st.write(pi_digits_list)

pi_digits_array = np.array(pi_digits_list)

counts = np.bincount(pi_digits_array)

fig, ax = plt.subplots()

ax.barh(range(10), counts, align = 'center',
        edgecolor = [0.6, 0.6, 0.6])

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.set_xlabel('Count')
ax.set_ylabel('Digit, 0~9')
plt.yticks(range(10))

st.pyplot(fig)


    