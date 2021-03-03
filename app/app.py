import streamlit as st

st.markdown("<h1 style='text-align: center; color: red;'>FakeOrNot</h1>", unsafe_allow_html=True)

st.text_input("Headline from the News: ")

if st.button("Verify"):
    st.markdown("""
    <h3 style='text-align: center;'>
    RESULT
    </h3>""", unsafe_allow_html=True)

else:
    st.markdown("""
    <h3 style='text-align: center;'>
    RESULT
    </h3>""", unsafe_allow_html=True)

st.markdown("""
<p style='text-align: center;'>
Made with 💜 by <a href="https://github.com/gabrielmayers">Gabriel Mayer</a> </p>"""
, unsafe_allow_html=True)
