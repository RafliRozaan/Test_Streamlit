import streamlit as st
import pandas as pd
import numpy as np
from streamlit_autorefresh import st_autorefresh
from streamlit_autorefresh import st_autorefresh


count = st_autorefresh(interval=2000, limit=100, key="fizzbuzzcounter")

st.title("Litho Facies Prediction Module")
st.text("Predict lithofacies from well log module")
st.text("")

st.subheader("Lithofacies Prediction Model Performance Test")
st.text("Generate precomputed prediction results of 10 different wells.")
st_ms = st.selectbox("Well Name",('A','B','C'),key='one')
generate_1 = st.button('Generate Prediction',key='but1')

st.subheader("Lithofacies Prediction from Well Log Data")
st.text("Show model performance on 10 sample wells.")
st_ms_2 = st.selectbox("Well Name",('A','B','C'),key='two')
generate_2 = st.button('Generate Precomputed Result',key='but2')

st.subheader("Upload Well Log Dataset for Lithofacies Prediction")
st.text("Upload your own well log data for lithofacies prediction.")
file = st.file_uploader('WELL Log Data')
generate_3 = st.button('Generate Prediction',key='but3')