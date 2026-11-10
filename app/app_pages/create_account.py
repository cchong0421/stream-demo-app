import streamlit as st

st.title("Create account")

with st.form("create_account_form"):
    username = st.text_input("使用者名稱")
    email = st.text_input("電子信箱")
    submitted = st.form_submit_button("註冊帳號", width="content")

    if submitted:
        if username and email:
            st.success(f"帳號 {username} 建立成功！", title="完成")
        else:
            st.error("請輸入完整的使用者名稱與電子信箱。", title="欄位未完整填寫")
