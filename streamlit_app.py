import streamlit as st
import pandas as pd
import numpy as np

#import df from wavetest
from mywavetest import get_df

stdf = get_df()

st.title("WAvE CRS")
st.write(
    "Welcome to the WAvE Customer Reporting Service. Below is a bar chart of daily fatigue occurences."
)
st.write("We will be adding more data visualizations in the next few months. Stay tuned!")
st.table(stdf)
