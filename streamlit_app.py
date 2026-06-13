import streamlit as st
import pandas as pd
st.title('🎈 Fetal_health_prediction-app')

st.info('This is a featl health prediction app!')
with st.expander('data'):
  st.write('**Raw data**')
df = pd.read_csv("https://raw.githubusercontent.com/Finbarr234/Fetal_health_prediction-app/master/fetalhealth%20(1).csv")
df

st.write('**x**')
x = df.drop('fetal_health', axis=1)
x

st.write('**y**')
y = df['fetal_health']
y

with st.expander('data visualization'):
  st.scatter_chart(data=df, x='fetal_health', y='fetal_health', color='fetal_health')

import streamlit as st
import pandas as pd

st.title('🎈 Fetal Health Prediction App')

st.info('This is a fetal health prediction app!')

df = pd.read_csv(
"https://raw.githubusercontent.com/Finbarr234/Fetal_health_prediction-app/master/fetalhealth%20(1).csv"
)

with st.expander('Data'):
     st.write('Raw Data')
     st.dataframe(df.head())

st.write('Features (X)')
x = df.drop('fetal_health', axis=1)
st.dataframe(x.head())

st.write('Target (y)')
y = df['fetal_health']
st.write(y.head())

with st.expander('Data Visualization'):
     st.bar_chart(df['fetal_health'].value_counts())
