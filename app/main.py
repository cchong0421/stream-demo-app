import streamlit as st
import pandas as pd

pages = {
    "Demo": [
        st.Page("demo/learn.py", title="Dashboard", icon=":material/dashboard:", default=True),
        st.Page("demo/trial.py", title="Dashboard-2", icon=":material/dashboard:"),
        st.Page("demo/aboutMe.py", title="AboutMe", icon=":material/search:"),
    ],
    "Account": [
        st.Page("account/create_account.py", title="Create Account", icon=":material/search:"),
        st.Page("account/manage_account.py", title="Manage Account", icon=":material/search:"),
    ],
}

pg = st.navigation(pages)
pg.run()
