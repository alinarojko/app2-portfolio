import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=600)

with col2:
    st.title("Alina Rozhko")
    content = """🔴 Alina  – QA Engineer | Python Automation | Freelance 🔴

I am an experienced QA Engineer with a passion for quality and efficiency in software testing. Currently expanding my skills by learning Python for automation and freelance projects. My goal is to create reliable, scalable, and efficient testing solutions that streamline development and improve product quality.

With hands-on experience in manual and automated testing, I focus on delivering high-quality software through robust testing strategies. Always eager to learn, adapt, and implement the best practices in QA and automation. 🚀

📌 LinkedIn Profile"""
    st.write(content)

content2 = """Bellow you can find some of the apps I have built on Python. 
If you any additional queries -  Feel free to contact me!"""
st.write(content2)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])