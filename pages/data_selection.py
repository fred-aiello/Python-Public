import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as PLT
import pandas_datareader.data as wb
import datetime as dt
from datetime import datetime,timedelta


select_eq=st.multiselect('select equity',['AAPL','MSFT','TWTR','IBM','BAC','GS','JPM','MS','^GSPC','^FCHI'])
st.write('You selected ',select_eq)

start_date=dt.date.today()


col1, col2,col3, col4, col5,col6,col7,col8=st.columns(8)

with col1:
if st.button('1D'):
st.write(start_date)

with col2:
if st.button('5D'):
st.write(start_date+timedelta(days=-5))

with col3:
if st.button('1M'):
st.write(start_date+timedelta(months=-1))

with col4:
if st.button('6M'):
st.write(start_date+timedelta(months=-6))

with col5:
if st.button('YTD'):
st.write(start_date)

with col6:
if st.button('1Y'):
st.write(start_date)

with col7:
if st.button('5Y'):
st.write(start_date)

with col8:
if st.button('Max'):
st.write(start_date)




def delta_time(y,m,d):

timedelta(
