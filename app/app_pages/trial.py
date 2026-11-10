import streamlit as st

st.title("System alerts")

st.info("系統目前所有服務正常運作中。", title="服務狀態")

st.success("資料庫連線已建立且已載入最新報表快取。", title="連線成功")

st.warning("若需修改設定檔，請至 Account > Manage account 進行變更。", title="注意事項")
