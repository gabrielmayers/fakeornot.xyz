import streamlit as st

st.markdown("<h1 style='text-align: center; color: red;'>FakeOrNot</h1>", unsafe_allow_html=True)

st.text_input("Headline from the News: ")

st.button("Verify")

st.markdown("""
<p style='text-align: center;'>
Made with 💜 by <a href="https://github.com/gabrielmayers">Gabriel Mayer</a> </p>"""
, unsafe_allow_html=True)
