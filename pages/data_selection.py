import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as PLT
import pandas_datareader as wb
import datetime as dt
from datetime import datetime,timedelta
import investpy 

tickers = {
    "SP500": "^GSPC",
    "CAC40": "^FCHI",
    "Apple":'AAPL',
    "Twitter":'TWTR',
    "JP Morgan":'JPM',
}

def DataFrame_Norm(df):

    # Dataframe normalisation
    for i in range(0,len(df.columns)-1): df.iloc[:,i]=df.iloc[:,i].str.upper() 
    df.columns=df.columns.str.upper()
    
    return df

df=investpy.stocks.get_stocks(country=None)

DataFrame_Norm(df)

cty=np.sort(df.COUNTRY.unique()).tolist()

select_cty=st.sidebar.multiselect('select country',cty)

# Include tabs in the page
for i in range(0,len(select_cty)): 
    st.write(select_cty[i]) #tabi = st.tabs("chart_" & i)

'''
with tab1:
    st.header("Nice Chart")
    st.subheader("A tab with a chart")
    st.line_chart(data)
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

tickers=np.sort(df[df.COUNTRY.isin(select_cty)].NAME.unique()).tolist()

select_eq=st.multiselect('select equity',tickers)
selection= list([tickers[I] for I in select_eq])

st.write('Country ', select_cty)
st.write('Selected Equity ', select_eq) # investpy.stocks.get_stocks(country='France')) #None))


price_data=df[(df.name.isin(list_eq)) & (df.country==select_cty)]  

start_date=dt.date.today()
end_date = dt.datetime(1980,1,1) #(2013, 1,1) #1980, 1, 1)

#price_data = wb.DataReader(list(tickers.values()),'yahoo',end_date) ['Adj Close'] #'yahoo', start, end) ['Close']#['Adj Close']

#price_data.insert(0,'Date',price_data.index)

st.dataframe(price_data)

col1, col2,col3, col4, col5,col6,col7,col8=st.columns(8)
st.dataframe(price_data.loc[price_data['Date']==start_date])
st.write(len(price_data['Date'])==start_date)


with col1:
    if st.button('1D'):
      st.dataframe(price_data.filter(items=[start_date]))

with col2:
   if st.button('5D'):
     new_date=start_date-pd.DateOffset(days=5)
     st.dataframe(price_data.loc[price_data['Date']>= new_date])
    
with col3:
  if st.button('1M'):
    new_date=start_date-pd.DateOffset(months=1)
    st.dataframe(price_data.loc[price_data['Date']>= new_date])

with col4:
  if st.button('6M'):
    new_date=start_date-pd.DateOffset(months=6)
    st.dataframe(price_data[price_data.iloc[0]>=new_date])

with col5:
  if st.button('YTD'):
    new_date=dt.date(start_date.year,1,1)
    st.dataframe(price_data[price_data.iloc[0]>=new_date])



with col6:
  if st.button('1Y'):
    new_date=start_date-pd.DateOffset(years=1)
    st.dataframe(price_data[price_data.iloc[0]>=new_date])

with col7:
  if st.button('5Y'):
    new_date=start_date-pd.DateOffset(years=5)
    st.dataframe(price_data[price_data.iloc[0]>=new_date])

with col8:
  if st.button('Max'):
    new_date=start_date-pd.DateOffset(days=5)
    st.dataframe(price_data[price_data.iloc[0]>=new_date])



#print(list(tickers.keys()))

#['AAPL', 'NKE', 'GOOGL','AMZN']


 

df=price_data.copy()

df.columns=list(tickers.keys())

st.dataframe(df)

#def delta_time(y,m,d):

  #timedelta(
'''
