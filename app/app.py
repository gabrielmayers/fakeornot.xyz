import streamlit as st

st.markdown("<h1 style='text-align: center; color: red;'>FakeOrNot</h1>", unsafe_allow_html=True)

st.text_input("Headline from the News")

st.button("Verify")