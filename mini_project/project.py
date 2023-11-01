import os
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt

# Replace 'YOUR_API_KEY' with your Alpha Vantage API key
api_key = 'XMynEv7VE0XTznilqgm_HWpr_EapDwAo'

# Initialize Alpha Vantage API client
ts = TimeSeries(key=api_key, output_format='pandas')

# Define the stock symbol you want to fetch data for
symbol = 'AAPL'  # Example: Apple Inc.

# Fetch recent stock data (last 100 data points)
data, meta_data = ts.get_intraday(symbol=symbol, interval='1min', outputsize='compact')

# Extract and plot the close prices
data['4. close'].plot()
plt.title(f'Recent Stock Data for {symbol}')
plt.xlabel('Time')
plt.ylabel('Price (USD)')
plt.grid(True)

# Show the plot
plt.show()
