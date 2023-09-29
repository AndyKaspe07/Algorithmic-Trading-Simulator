# To download stock price info using yahoo API
import datetime as dt
import pandas_datareader.data as pdr
import yfinance as yf 

yf.pdr_override()


stock_symbols = ['FB']

end = dt.date.today()
start = dt.date.today() - dt.timedelta(days=3*365)

print(f'end date is {end}')
print(f'start date is {start}')

df = pdr.get_data_yahoo('GOOGL', start, end)

print(df.head())
