from pathlib import Path
import pandas as pd
import streamlit as st

DATA_FILE = Path(__file__).resolve().parent.parent / "ETFRank_202407.csv"

@st.cache_data
def load_data(file_path: Path) -> pd.DataFrame:
    df = pd.read_csv(
        file_path,
        dtype={
            "排序": "int",
            "股票代號": "string",
            "股票名稱": "string",
            "股票交易戶數": "int64",
            "ETF代號": "string",
            "ETF名稱": "string",
            "ETF交易戶數": "int64",
        },
    )
    df["StockIDName"] = df["股票代號"] + "-" + df["股票名稱"]
    df["ETFIDName"] = df["ETF代號"] + "-" + df["ETF名稱"]
    return df[["排序", "StockIDName", "股票交易戶數", "ETFIDName", "ETF交易戶數"]]


st.title("定期定額前十名交易戶數證券統計")

st.subheader("範例資料說明")
st.write(
    """
- 資料來源：[臺灣證券交易所 open_data](https://www.twse.com.tw/zh/ETFReport/ETFRank?response=open_data)
- 範例格式：
    ```csv
    排序,股票代號,股票名稱,股票交易戶數,ETF代號,ETF名稱,ETF交易戶數
    "1","2330","台積電","93074","00878","國泰永續高股息","292671"
    "2","2886","兆豐金","33100","0056","元大高股息","267916"
    "3","2884","玉山金","29920","0050","元大台灣50","254394"
    ```
"""
)

df = load_data(DATA_FILE)

st.divider()

st.subheader("顯示資料表")
st.dataframe(
    data=df,
    width="stretch",
    hide_index=True,
    alt="定期定額前十名交易戶數證券與 ETF 統計資料表",
)

st.divider()

st.subheader("定期定額前十大交易股票")
stock_chart_data = df[["StockIDName", "股票交易戶數"]]
st.bar_chart(
    stock_chart_data,
    x="StockIDName",
    y="股票交易戶數",
    x_label="股票名稱",
    height=500,
    alt="定期定額前十大交易股票戶數長條圖",
)

st.divider()

st.subheader("ETF 定期定額前十大交易標的")
etf_chart_data = df[["ETFIDName", "ETF交易戶數"]]
st.bar_chart(
    etf_chart_data,
    x="ETFIDName",
    y="ETF交易戶數",
    x_label="ETF 股票名稱",
    height=500,
    alt="ETF 定期定額前十大交易戶數長條圖",
)
