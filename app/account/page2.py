import streamlit as st

st.set_page_config(layout="wide")

st.title("Page 2")

sentiment_mapping = ["one", "two", "three", "four", "five"]
selected = st.feedback("stars")
if selected is not None:
    st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")