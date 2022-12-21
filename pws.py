import streamlit as st

st.set_page_config(page_title="Title for my page", layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("./images/photo.png", width=900) 

with col2:
    st.title("My name goes here, eventually")
    content = ("""Write something about 
    yourself here""")
    st.info(content)

