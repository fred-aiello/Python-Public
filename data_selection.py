import pandas as pd
import numpy as np
import matplotlib.pyplot as PLT
import pandas_datareader.data as wb
import datetime as dt
from datetime import datetime,timedelta


select_eq=st.multiselect('AAPL','MSFT','TWTR','IBM','BAC','GS','JPM','MS','^FCHI')
st.markdown('selection ',select_eq)

