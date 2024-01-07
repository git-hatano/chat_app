"""
streamlit run 00_my_first_app.py
"""
import streamlit as st
import pandas as pd
import numpy as np

st.write("Hello world. Let's learn how to build a AI-based app together.")

arr = np.zeros((3, 10))
df = pd.DataFrame(arr)
st.write(df)
