import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=600)

with col2:
    st.title("Alina Rozhko")
    content = """"Alina Rozhko – QA Engineer with experience in testing and automation. 
    Learning Python and applying it to develop reliable and high-quality solutions."""
    st.write(content)
