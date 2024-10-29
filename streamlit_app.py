import streamlit as st
import pandas as pd
import numpy as np

st.title("WAvE CRS")
st.write(
    "Welcome to the WAvE Customer Reporting Service. Below is a bar chart of daily fatigue occurences."
)
st.write("We will be adding more data visualizations in the next few months. Stay tuned!")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.bar_chart(chart_data)
