from email.utils import parsedate_to_datetime
import streamlit as st
import datetime
import pandas as pd

st.set_page_config(layout="wide")

st.title("OA 需求單查詢")

today = datetime.datetime.now()
today_add_2 = today + datetime.timedelta(days=2)

# datetime columns
col_dates = [   '申請日', '預計完成日'  ]
date_formats = {    '申請日': '%Y/%m/%d',
                    '預計完成日': '%Y/%m/%d'}

df = pd.read_csv('app/oareq/oareq.csv', 
                 parse_dates=col_dates, 
                 date_format=date_formats, 
                 encoding='utf-8',
                 dtype={
    "表單編號": 'string',
    "狀態": 'string',
    "申請單位": 'string',
    "申請日": 'string',
    "申請人": 'string',
    "系統": 'string',
    "完整需求內容": 'string',
    "承辦人員": 'string',
    "預計完成日": 'string',
    "UAT單": 'string',
    "換版單": 'string',
    "預估工時": 'string',
})


## 轉換欄位值內容
df['申請單位'] = [ d.replace('-','\r\n') if '-' in d else d for d in df['申請單位']]
df['完整需求內容'] = [ d[:20] + " ....(More)" if len(d)> 20 else d for d in df['完整需求內容']]

# df['申請日'] = pd.to_datetime(df['預計完成日'], format='%Y/%m/%d', errors='coerce')
# df['預計完成日'] = pd.to_datetime(df['預計完成日'], format='%Y/%m/%d', errors='coerce')

# 判斷日期是否為空值，若為空值則轉成空字串，否則回值日期字串 YYYY/mm/dd
# df['申請日'] = [d.strftime('%Y/%m/%d') if not pd.isnull(d) else '' for d in df['申請日']]
# df['預計完成日'] = [d.strftime('%Y/%m/%d') if not pd.isnull(d) else '' for d in df['預計完成日']]

with st.expander(label="說明:「Search」功能可以找尋目前資料中的所有關鍵字。", expanded=True, icon=":material/search:"):
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        dStart = st.date_input("申請日期(起)", value=today)
        dEnd = st.date_input("(迄)", value=today_add_2)

    with col2:
        statusOptions = st.multiselect(
            "表單狀態",
            options=["全部", "進行中", "已結案", "駁回結束", "起單人撤回"],
            default=["全部"],
            max_selections=1
        )
    with col3:
        oareqNo = st.text_input("表單編號", placeholder="請輸入需求單號")

    with col4:
        TeamOptions = st.multiselect(
            "承辦科組",
            ["全部", "證券支援科", "證券期貨科", "開放系統科", "電子系統科"],
            ["全部"],
        )
    queryButton = st.button("查詢")


# st.write("You selected:", statusOptions, dStart, dEnd, oareqNo)
# # selectdf = st.dataframe(data=df, hide_index=True, use_container_width=True, selection_mode=["single-row"], on_select="rerun")
    
def filter_by_daterange(df, start: str, end: str) -> pd.DataFrame:
    # print(f"Start: {start}, End: {end}, Diff: { (end - start).days}")
    # # Below are the quick examples

    # # Example 1: Select DataFrame rows between two dates
    # mask = (df['InsertedDates'] > start_date) & (df['InsertedDates'] <= end_date)
    # df2 = df.loc[mask]

    # # Example 2: Using pandas.DataFrame.loc[] to Filter Rows by Dates
    # df2 = df.loc[between_two_dates]

    # # Example 3: Using pandas.DataFrame.query() to select DataFrame Rows
    # start_date = '2021-11-15'
    # end_date   = '2021-11-18'
    # df2 = df.query('InsertedDates >= @start_date and InsertedDates <= @end_date')

    # # Example 4: Select rows between two dates using DataFrame.query()
    # start_date = '2021-11-15'
    # end_date = '2021-11-18'
    # df2 = df.query('InsertedDates > @start_date and InsertedDates < @end_date')

    # # Example 5: Pandas.Series.between() function Using two dates
    # df2 = df.loc[df["InsertedDates"].between("2021-11-16", "2021-11-18")]

    # # Example 6: Select DataFrame rows between two dates using DataFrame.isin()
    # df2 = df[df["InsertedDates"].isin(pd.date_range("2021-11-15", "2021-11-17"))]
    if (end - start).days >= 0:
        startdate = start
        enddate = end
        # startdate = pd.to_datetime(start, format='%Y-%m-%d', errors='coerce').date()
        # enddate = pd.to_datetime(end, format='%Y-%m-%d', errors='coerce').date()
        print(f"startdate: {startdate} , type(startdate): {type(startdate)} , enddate: {enddate} , type(enddate): {type(enddate)}")
        daterange_filtered_df = df
        # daterange_filtered_df = df.loc[df["申請日"].between(startdate, enddate)]
        # daterange_filtered_df = df.query('申請日 >= @start and 申請日 <= @end')
    else:
        daterange_filtered_df = df

    return daterange_filtered_df

def filter_by_status(df, options) -> pd.DataFrame:
    if len(options) == 0 or options[0] == '全部':
        filtered_df = df
    else:
        filtered_df = df[df['狀態'].isin(options)]
    return filtered_df

if queryButton:
   
    filtered_df = filter_by_daterange(df, dStart, dEnd)
    # filtered_df = filter_by_status(filtered_df, statusOptions)
    st.dataframe(filtered_df, use_container_width=True, hide_index=True)
    #st.dataframe(df, use_container_width=True, hide_index=True)
    # st.dataframe(filtered_df, use_container_width=True, hide_index=True , column_config={
    #     "申請日": st.column_config.DatetimeColumn(
    #         "申請日",
    #         format="YYYY/MM/DD",
    #     ),
    #     "預計完成日": st.column_config.DatetimeColumn(
    #         "預計完成日",
    #         format="YYYY/MM/DD",
    #     ),
    # },)
