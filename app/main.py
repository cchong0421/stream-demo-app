import streamlit as st

st.set_page_config(
    page_title="Streamlit Demo App",
    page_icon=":material/analytics:",
    layout="wide",
    initial_sidebar_state="expanded",
)

dashboard = st.Page(
    "app_pages/learn.py",
    title="Dashboard",
    icon=":material/dashboard:",
    default=True,
    help="定期定額前十名交易戶數證券與 ETF 統計報表",
)

aboutme = st.Page(
    "app_pages/about_me.py",
    title="About me",
    icon=":material/person:",
    help="關於本專案說明與作者資訊",
)

create_account = st.Page(
    "app_pages/create_account.py",
    title="Create account",
    icon=":material/person_add:",
    help="註冊新帳號",
)

manage_account = st.Page(
    "app_pages/manage_account.py",
    title="Manage account",
    icon=":material/manage_accounts:",
    help="管理現有帳號與偏好設定",
)

trialpage = st.Page(
    "app_pages/trial.py",
    title="System alerts",
    icon=":material/notifications:",
    help="系統提示與警報展示",
)

feedback = st.Page(
    "app_pages/feedback.py",
    title="Feedback",
    icon=":material/rate_review:",
    help="使用者評分與回饋收集",
)

pg = st.navigation(
    {
        "Reports": [dashboard],
        "Account": [aboutme, create_account, manage_account],
        "Tools": [trialpage, feedback],
    }
)

pg.run()
