import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as PLT
import pandas_datareader as wb
import datetime as dt
from datetime import datetime,timedelta
import investpy 
import flag

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
# Preparation country flags

flag_cty={
    'AFGHANISTAN':'AF',
    'ÅLAND ISLANDS':'AX',
    'ALBANIA':'AL',
    'ALGERIA':'DZ',
    'AMERICAN SAMOA':'AS',
    'ANDORRA':'AD',
    'ANGOLA':'AO',
    'ANGUILLA':'AI',
    'ANTARCTICA':'AQ',
    'ANTIGUA & BARBUDA':'AG',
    'ARGENTINA':'AR',
    'ARMENIA':'AM',
    'ARUBA':'AW',
    'ASCENSION ISLAND':'AC',
    'AUSTRALIA':'AU',
    'AUSTRIA':'AT',
    'AZERBAIJAN':'AZ',
    'BAHAMAS':'BS',
    'BAHRAIN':'BH',
    'BANGLADESH':'BD',
    'BARBADOS':'BB',
    'BELARUS':'BY',
    'BELGIUM':'BE',
    'BELIZE':'BZ',
    'BENIN':'BJ',
    'BERMUDA':'BM',
    'BHUTAN':'BT',
    'BOLIVIA':'BO',
    'BOSNIA':'BA',
    'BOTSWANA':'BW',
    'BOUVET ISLAND':'BV',
    'BRAZIL':'BR',
    'BRITISH INDIAN OCEAN TERRITORY':'IO',
    'BRITISH VIRGIN ISLANDS':'VG',
    'BRUNEI':'BN',
    'BULGARIA':'BG',
    'BURKINA FASO':'BF',
    'BURUNDI':'BI',
    'CAMBODIA':'KH',
    'CAMEROON':'CM',
    'CANADA':'CA',
    'CANARY ISLANDS':'IC',
    'CAPE VERDE':'CV',
    'CARIBBEAN NETHERLANDS':'BQ',
    'CAYMAN ISLANDS':'KY',
    'CENTRAL AFRICAN REPUBLIC':'CF',
    'CEUTA & MELILLA':'EA',
    'CHAD':'TD',
    'CHILE':'CL',
    'CHINA':'CN',
    'CHRISTMAS ISLAND':'CX',
    'CLIPPERTON ISLAND':'CP',
    'COCOS (KEELING) ISLANDS':'CC',
    'COLOMBIA':'CO',
    'COMOROS':'KM',
    'CONGO - BRAZZAVILLE':'CG',
    'CONGO - KINSHASA':'CD',
    'COOK ISLANDS':'CK',
    'COSTA RICA':'CR',
    'CROATIA':'HR',
    'CUBA':'CU',
    'CURAÇAO':'CW',
    'CYPRUS':'CY',
    'CZECHIA':'CZ',
    'DENMARK':'DK',
    'DIEGO GARCIA':'DG',
    'DJIBOUTI':'DJ',
    'DOMINICA':'DM',
    'DOMINICAN REPUBLIC':'DO',
    'ECUADOR':'EC',
    'EGYPT':'EG',
    'EL SALVADOR':'SV',
    'EQUATORIAL GUINEA':'GQ',
    'ERITREA':'ER',
    'ESTONIA':'EE',
    'ESWATINI':'SZ',
    'ETHIOPIA':'ET',
    'EUROPEAN UNION':'EU',
    'FALKLAND ISLANDS':'FK',
    'FAROE ISLANDS':'FO',
    'FIJI':'FJ',
    'FINLAND':'FI',
    'FRANCE':'FR',
    'FRENCH GUIANA':'GF',
    'FRENCH POLYNESIA':'PF',
    'FRENCH SOUTHERN TERRITORIES':'TF',
    'GABON':'GA',
    'GAMBIA':'GM',
    'GEORGIA':'GE',
    'GERMANY':'DE',
    'GHANA':'GH',
    'GIBRALTAR':'GI',
    'GREECE':'GR',
    'GREENLAND':'GL',
    'GRENADA':'GD',
    'GUADELOUPE':'GP',
    'GUAM':'GU',
    'GUATEMALA':'GT',
    'GUERNSEY':'GG',
    'GUINEA':'GN',
    'GUINEA-BISSAU':'GW',
    'GUYANA':'GY',
    'HAITI':'HT',
    'HEARD & MCDONALD ISLANDS':'HM',
    'HONDURAS':'HN',
    'HONG KONG':'HK',
    'HUNGARY':'HU',
    'ICELAND':'IS',
    'INDIA':'IN',
    'INDONESIA':'ID',
    'IRAN':'IR',
    'IRAQ':'IQ',
    'IRELAND':'IE',
    'ISLE OF MAN':'IM',
    'ISRAEL':'IL',
    'ITALY':'IT',
    'IVORY COAST':'CI',
    'JAMAICA':'JM',
    'JAPAN':'JP',
    'JERSEY':'JE',
    'JORDAN':'JO',
    'KAZAKHSTAN':'KZ',
    'KENYA':'KE',
    'KIRIBATI':'KI',
    'KOSOVO':'XK',
    'KUWAIT':'KW',
    'KYRGYZSTAN':'KG',
    'LAOS':'LA',
    'LATVIA':'LV',
    'LEBANON':'LB',
    'LESOTHO':'LS',
    'LIBERIA':'LR',
    'LIBYA':'LY',
    'LIECHTENSTEIN':'LI',
    'LITHUANIA':'LT',
    'LUXEMBOURG':'LU',
    'MACAO SAR CHINA':'MO',
    'MADAGASCAR':'MG',
    'MALAWI':'MW',
    'MALAYSIA':'MY',
    'MALDIVES':'MV',
    'MALI':'ML',
    'MALTA':'MT',
    'MARSHALL ISLANDS':'MH',
    'MARTINIQUE':'MQ',
    'MAURITANIA':'MR',
    'MAURITIUS':'MU',
    'MAYOTTE':'YT',
    'MEXICO':'MX',
    'MICRONESIA':'FM',
    'MOLDOVA':'MD',
    'MONACO':'MC',
    'MONGOLIA':'MN',
    'MONTENEGRO':'ME',
    'MONTSERRAT':'MS',
    'MOROCCO':'MA',
    'MOZAMBIQUE':'MZ',
    'MYANMAR (BURMA)':'MM',
    'NAMIBIA':'NA',
    'NAURU':'NR',
    'NEPAL':'NP',
    'NETHERLANDS':'NL',
    'NEW CALEDONIA':'NC',
    'NEW ZEALAND':'NZ',
    'NICARAGUA':'NI',
    'NIGER':'NE',
    'NIGERIA':'NG',
    'NIUE':'NU',
    'NORFOLK ISLAND':'NF',
    'NORTH KOREA':'KP',
    'NORTH MACEDONIA':'MK',
    'NORTHERN MARIANA ISLANDS':'MP',
    'NORWAY':'NO',
    'OMAN':'OM',
    'PAKISTAN':'PK',
    'PALAU':'PW',
    'PALESTINIAN TERRITORIES':'PS',
    'PANAMA':'PA',
    'PAPUA NEW GUINEA':'PG',
    'PARAGUAY':'PY',
    'PERU':'PE',
    'PHILIPPINES':'PH',
    'PITCAIRN ISLANDS':'PN',
    'POLAND':'PL',
    'PORTUGAL':'PT',
    'PUERTO RICO':'PR',
    'QATAR':'QA',
    'REUNION':'RE',
    'ROMANIA':'RO',
    'RUSSIA':'RU',
    'RWANDA':'RW',
    'SAMOA':'WS',
    'SAN MARINO':'SM',
    'SÃO TOME & PRINCIPE':'ST',
    'SAUDI ARABIA':'SA',
    'SENEGAL':'SN',
    'SERBIA':'RS',
    'SEYCHELLES':'SC',
    'SIERRA LEONE':'SL',
    'SINGAPORE':'SG',
    'SINT MAARTEN':'SX',
    'SLOVAKIA':'SK',
    'SLOVENIA':'SI',
    'SOLOMON ISLANDS':'SB',
    'SOMALIA':'SO',
    'SOUTH AFRICA':'ZA',
    'SOUTH GEORGIA & SOUTH SANDWICH ISLANDS':'GS',
    'SOUTH KOREA':'KR',
    'SOUTH SUDAN':'SS',
    'SPAIN':'ES',
    'SRI LANKA':'LK',
    'ST. BARTHELEMY':'BL',
    'ST. HELENA':'SH',
    'ST. KITTS & NEVIS':'KN',
    'ST. LUCIA':'LC',
    'ST. MARTIN':'MF',
    'ST. PIERRE & MIQUELON':'PM',
    'ST. VINCENT & GRENADINES':'VC',
    'SUDAN':'SD',
    'SURINAME':'SR',
    'SVALBARD & JAN MAYEN':'SJ',
    'SWEDEN':'SE',
    'SWITZERLAND':'CH',
    'SYRIA':'SY',
    'TAIWAN':'TW',
    'TAJIKISTAN':'TJ',
    'TANZANIA':'TZ',
    'THAILAND':'TH',
    'TIMOR-LESTE':'TL',
    'TOGO':'TG',
    'TOKELAU':'TK',
    'TONGA':'TO',
    'TRINIDAD & TOBAGO':'TT',
    'TRISTAN DA CUNHA':'TA',
    'TUNISIA':'TN',
    'TURKEY':'TR',
    'TURKMENISTAN':'TM',
    'TURKS & CAICOS ISLANDS':'TC',
    'TUVALU':'TV',
    'U.S. OUTLYING ISLANDS':'UM',
    'U.S. VIRGIN ISLANDS':'VI',
    'UGANDA':'UG',
    'UKRAINE':'UA',
    'UNITED ARAB EMIRATES':'AE',
    'UNITED KINGDOM':'GB',
    'UNITED NATIONS':'UN',
    'UNITED STATES':'US',
    'URUGUAY':'UY',
    'UZBEKISTAN':'UZ',
    'VANUATU':'VU',
    'VATICAN CITY':'VA',
    'VENEZUELA':'VE',
    'VIETNAM':'VN',
    'WALLIS & FUTUNA':'WF',
    'WESTERN SAHARA':'EH',
    'YEMEN':'YE',
    'ZAMBIA':'ZM',
    'ZIMBABWE':'ZW'
         }

df=investpy.stocks.get_stocks(country=None)




DataFrame_Norm(df)

# Country selection
cty=np.sort(df.COUNTRY.unique()).tolist()

with st.sidebar:
    st.title('Select your period')
    start_date = st.date_input("Start Date", value=pd.to_datetime("1980-01-01", format="%Y-%m-%d"))
    end_date = st.date_input("End Date", value=pd.to_datetime(datetime.today(), format="%Y-%m-%d"))
    
    st.title('select country')
    select_cty=st.sidebar.multiselect('select country',cty)
    st.write (len(select_cty))



# List collecting selected countries to create tabs
L=[]

# Include tabs in the page
for i in range(len(select_cty)): L.append(flag.flag(flag_cty.get(select_cty[i])) + ' ' + select_cty[i]) 
tabs=st.tabs(L)       
st.write('Init:',len(select_cty))
for i in range(len(select_cty)):
          
    with st.sidebar:     
        st.title(select_cty[i])
        tickers=np.sort(df[df.COUNTRY==select_cty[i]].NAME.unique()).tolist()
        select_eq=st.multiselect('select equity',tickers)

        #st.date_input("Select start date", datetime.date(1980, 1, 1))
        #st.date_input("Select end date", datetime.date(datetime.today()))
            
    st.write(i)
    
    with tabs[i]:
        st.header(flag.flag(flag_cty.get(select_cty[i])) + " Equity")
        st.subheader("List of Equities :")
        eq_cod=df[(df.COUNTRY==select_cty[i]) & (df.NAME.isin(select_eq))].SYMBOL
        st.write(eq_cod)
        dg=investpy.stocks.get_stock_historical_data(
            stock=eq_cod,
            country=select_cty[i],
            from_date=start_date,
            to_date=end_date,
       #     order=descending
        )
        st.dataframe(dg)
            
tabs=st.tabs(L)  

'''
for i in len(select_cty):
    with tabs[1]:
    st.header(flag.flag("AR") + "Nice Chart")
    st.subheader("A tab with a chart")
    #st.line_chart(data)
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)


st.tabs(['Tab number %d' %i for i in range(10)])
for i in range(0,len(select_cty)): 
    
    L.append(select_cty[i])
    tab1 = st.tabs(L) #st.write(select_cty[i]) 
    st.write(type(tab1))

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


price_data=df[(df.name==(list_eq)) & (df.country==select_cty)]  

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
