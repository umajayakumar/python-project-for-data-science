import yfinance as yf
import pandas as pd

GameStop=yf.Ticker("GME")
print(GameStop)
GameStop_info = GameStop.info
print(GameStop_info)
GameStop_data=GameStop.history(period="max")
print(GameStop_data)
df=GameStop_data.reset_index(inplace=True)
print("First Five Rows")
print(GameStop_data.head(5))