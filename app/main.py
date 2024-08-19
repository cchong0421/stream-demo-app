import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title("定期定額前十名交易戶數證券統計")

st.subheader("範例資料")
st.write(
"""
- Data Url : https://www.twse.com.tw/zh/ETFReport/ETFRank?response=open_data

- Sample Data:

    ```csv
    排序,股票代號,股票名稱,股票交易戶數,ETF代號,ETF名稱,ETF交易戶數
    "1","2330","台積電","93074","00878","國泰永續高股息","292671"
    "2","2886","兆豐金","33100","0056","元大高股息","267916"
    "3","2884","玉山金","29920","0050","元大台灣50","254394"
    ```

"""
)

df = pd.read_csv('app/ETFRank_202407.csv', dtype={
    '排序': 'int',
    '股票代號': 'string',
    '股票名稱': 'string',
    '股票交易戶數': 'int64',
    'ETF代號': 'string',
    'ETF名稱': 'string',
    'ETF交易戶數': 'int64'
})

# df = pd.read_csv('https://www.twse.com.tw/zh/ETFReport/ETFRank?response=open_data', dtype={
#     '排序': 'int',
#     '股票代號': 'string',
#     '股票名稱': 'string',
#     '股票交易戶數': 'int64',
#     'ETF代號': 'string',
#     'ETF名稱': 'string',
#     'ETF交易戶數': 'int64'
# })

df["StockIDName"] = df['股票代號'] + "-" + df['股票名稱']
df["ETFIDName"] = df['ETF代號'] + "-" + df['ETF名稱']

df = df[['排序','StockIDName', '股票交易戶數', 'ETFIDName', 'ETF交易戶數']]

st.divider()

st.subheader("顯示資料表")
# st.write(df)

# st.dataframe(data=None, width=None, height=None, *, use_container_width=False, hide_index=None, column_order=None, column_config=None, key=None, on_select="ignore", selection_mode="multi-row")
st.dataframe(data=df, width=None, use_container_width=True, hide_index=True)

#########################################################################################################
### Display <hr> Line
#########################################################################################################
st.divider()  

st.subheader("定期定額前十大交易股票")

chart_data = df[['StockIDName','股票交易戶數']]

st.bar_chart(chart_data, x="StockIDName", y="股票交易戶數", x_label="股票名稱", height=600)

#########################################################################################################
### Display <hr> Line
#########################################################################################################
st.divider()

st.subheader("ETF 定期定額前十大交易股票")

chart_data = df[['ETFIDName','ETF交易戶數']]

st.bar_chart(chart_data, x="ETFIDName", y="ETF交易戶數", x_label="ETF 股票名稱", height=600)
