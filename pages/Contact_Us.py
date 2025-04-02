import streamlit as st

st.header("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Your email address", key="email")
    massage = st.text_area("Your message")
    button = st.form_submit_button("Submit")
    if button:
        print("I was pressed ")
