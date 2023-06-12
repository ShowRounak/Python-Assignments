import streamlit as st
import pandas as pd
import time

st.title('Startup Dashboard')
st.header('Welcome to the Startup Project')
st.subheader('Data Analysis project')

st.write('This is a normal text')
st.markdown("""
### My favorite Startups
- Paytm
- Zomato
- Zerodha
""")

st.code("""
def square(num):
    return num**2
""")

st.latex('x^2+y^2 +6 = 0')

df = pd.DataFrame({
    'name': ['rounak', 'surajit', 'rudra', 'tapa'],
    'surname': ['show', 'nandi', 'chatterjee', 'banerjee']
})

st.dataframe(df)

st.metric('Revenue', 'Rs 3L', '3%')

st.json({
    'name': ['rounak', 'surajit', 'rudra', 'tapa'],
    'surname': ['show', 'nandi', 'chatterjee', 'banerjee']
})

st.image('glow.png')

st.sidebar.title('Sidebar Title')

col1, col2 = st.columns(2)

with col1:
    st.image('glow.png')
with col2:
    st.image('glow.png')

st.error('Login failed')
st.success('Successfully Login')

# bar = st.progress(0)
#
# for i in range(1,101):
#     time.sleep(0.1)
#     bar.progress(i)

email = st.text_input('Enter Email')
age = st.number_input('Enter Age')
DOB = st.date_input('Enter Date of Birth')

email = st.text_input('Enter Email')
password = st.text_input('Enter Password')
gender = st.selectbox('Select Gender', ['Male', "Female"])

login = st.button('Login')

if login:
    if email == 'rikbale@gmail.com' and password == '1234':
        st.success('Login successful')
        st.balloons()
        st.write(gender)
    else:
        st.error('Login Failed')

file = st.file_uploader('Upload a csv file')

if file is not None:
    df = pd.read_csv(file)
    st.dataframe(df.describe())
