import streamlit as st
from tokenizer import lets_token
from model import load_model

model = load_model()

st.markdown("<h1 style='text-align: center; color: red;'>FakeOrNot</h1>", unsafe_allow_html=True)

user_input = st.text_input("Headline from the News: ")

if st.button("Verify"):

    headline = [user_input]

    headline = lets_token(headline)

    pred = model.predict(headline)

    print(pred)

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
