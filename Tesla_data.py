import yfinance as yf
import pandas as pd

Tesla=yf.Ticker("TSLA")
print(Tesla)
Tesla_info = Tesla.info
print(Tesla_info)
tesla_data=Tesla.history(period="max")
print(tesla_data)
df=tesla_data.reset_index(inplace=True)
print("First Five Rows")
print(tesla_data.head(5))
