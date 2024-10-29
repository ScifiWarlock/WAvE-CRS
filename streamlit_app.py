import streamlit as st
import pandas as pd
import numpy as np
import subprocess
from subprocess import run

#import df from mywavetest
#from mywavetest import get_df

stdf = pd.read_excel("df.xlsx")

stdf = stdf.iloc[:, [-1]]

st.title("WAvE CRS")
st.write(
    "Welcome to the WAvE Customer Reporting Service. Below is a table of daily fatigue occurences."
)
st.write("We will be adding more data visualizations in the next few months. Stay tuned!")
st.table(stdf)

#subprocess.run("git commit")
#subprocess.run("git push")
