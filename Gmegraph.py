import yfinance as yf
import matplotlib.pyplot as plt

# Define the start and end dates of the data you want to download
start_date = '2010-01-01'
end_date = '2021-06-30'

# Download Tesla's stock data and revenue using yfinance
gme_data = yf.download('GME', start_date, end_date)

# Plot the closing prices for Tesla stock
plt.plot(gme_data["Close"])
plt.title("Gamestop Stock Prices")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.show()