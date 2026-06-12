import streamlit as st
import pandas as pd
st.title('🎈 Fetal_health_prediction-app')

st.info('This is a featl health prediction app!')
with st.expander('data'):
  st.write('**Raw data**')
df = pd.read_csv("https://raw.githubusercontent.com/Finbarr234/Fetal_health_prediction-app/master/fetalhealth%20(1).csv")
df

st.write('**x**')
x = df.drop('baseline value', axis=1)
x

st.write('**y**')
y = df.baseline value
y
