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

def delta_time(y,m,d):
timedelta(
