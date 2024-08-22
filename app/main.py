import streamlit as st
import pandas as pd


dashboard = st.Page(
    "demo/learn.py", title="Dashboard", icon=":material/dashboard:", default=True
)
trialpage = st.Page(
    "demo/trial.py", title="System alerts", icon=":material/notification_important:"
)
aboutme = st.Page("demo/aboutMe.py", title="AboutMe", icon=":material/search:")

pg = st.navigation(
    {
        "Reports": [dashboard],
        "Account": [aboutme],
        "Tools": [trialpage],
    }
).run()
