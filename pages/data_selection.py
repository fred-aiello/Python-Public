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
selection= [tickers[I] for I in select_eq]
st.write('You selected ', list(selection))

start_date=dt.date.today()
end_date = dt.datetime(1980,1,1) #(2013, 1,1) #1980, 1, 1)

price_data = wb.DataReader(list(tickers.values()),

                        'yahoo',end_date) ['Adj Close'] #'yahoo', start, end) ['Close']#['Adj Close']


col1, col2,col3, col4, col5,col6,col7,col8=st.columns(8)

with col1:
    if st.button('1D'):
      st.dataframe(price_data.loc[price_data['Date']<=start_date])

with col2:
   if st.button('5D'):
     new_date=start_date-pd.DateOffset(days=5)
     st.write(new_date.date())

with col3:
  if st.button('1M'):
    new_date=start_date-pd.DateOffset(months=1)
    st.write(new_date.date())

with col4:
  if st.button('6M'):
    new_date=start_date-pd.DateOffset(months=6)
    st.write(new_date.date())

with col5:
  if st.button('YTD'):
    new_date=dt.date(start_date.year,1,1)
    st.write(new_date.date())



with col6:
  if st.button('1Y'):
    new_date=start_date-pd.DateOffset(years=1)
    st.write(new_date.date())

with col7:
  if st.button('5Y'):
    new_date=start_date-pd.DateOffset(years=5)
    st.write(new_date.date())

with col8:
  if st.button('Max'):
    new_date=start_date-pd.DateOffset(days=5)
    st.write(new_date.date())
start_date)



#print(list(tickers.keys()))

#['AAPL', 'NKE', 'GOOGL','AMZN']


 

df=price_data.copy()

df.columns=list(tickers.keys())

st.dataframe(df)

#def delta_time(y,m,d):

  #timedelta(
