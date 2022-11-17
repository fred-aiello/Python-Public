import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as PLT
import pandas_datareader as wb
import datetime as dt
from datetime import datetime,timedelta

tickers = {
    "SP500": "^GSPC",
    "CAC40": "^FCHI",
    "Apple":'AAPL',
    "Twitter":'TWTR',
    "JP Morgan":'JPM',
}


select_eq=st.multiselect('select equity',tickers)

st.write('You selected ', [tickers[I] for I in select_eq])

start_date=dt.date.today()


col1, col2,col3, col4, col5,col6,col7,col8=st.columns(8)

with col1:
    if st.button('1D'):
      st.write(start_date)

with col2:
   if st.button('5D'):
     new_date=start_date-pd.DateOffset(days=5)
     st.write(new_date.date())

with col3:
  if st.button('1M'):
    st.write(start_date-pd.DateOffset(months=1))

with col4:
  if st.button('6M'):
    st.write(start_date-pd.DateOffset(months=6))

with col5:
  if st.button('YTD'):
    st.write(dt.date(start_date.year,1,1))

with col6:
  if st.button('1Y'):
    st.write(start_date-pd.DateOffset(years=1))

with col7:
  if st.button('5Y'):
    st.write(start_date-pd.DateOffset(years=5))

with col8:
  if st.button('Max'):
    st.write(start_date)


start = dt.datetime(1980,1,1) #(2013, 1,1) #1980, 1, 1)
end = dt.datetime(2022, 10, 1)

tickers = {
    "SP500": "^GSPC",
    "CAC40": "^FCHI",
}

print(list(tickers.keys()))

#['AAPL', 'NKE', 'GOOGL','AMZN']

price_data = web.DataReader(list(tickers.values()),

                        'yahoo',start) ['Adj Close'] #'yahoo', start, end) ['Close']#['Adj Close']

 

df=price_data.copy()

df.columns=list(tickers.keys())

st.dataframe(df)

#def delta_time(y,m,d):

  #timedelta(
