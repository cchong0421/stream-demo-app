import streamlit as st

st.title("Feedback")

sentiment_mapping = ["One", "Two", "Three", "Four", "Five"]
selected = st.feedback("stars")

if selected is not None:
    st.markdown(f"感謝您的回饋！您給予了 **{sentiment_mapping[selected]}** 顆星。")
