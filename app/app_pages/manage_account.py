import streamlit as st

st.title("Manage account")

st.write("在此頁面管理您的帳號設定與權限。")

with st.container(border=True):
    st.subheader("基本偏好設定")
    st.toggle("接收定期定額交易報表通知", value=True)
    st.toggle("啟用深色模式偏好", value=False)
