# filename: get_stock_data.py
import yfinance as yf
import matplotlib.pyplot as plt

# Download historical data for META and TSLA
meta = yf.download("META", start="2023-01-01", end="2024-01-01")
tesla = yf.download("TSLA", start="2023-01-01", end="2024-01-01")

# Extract closing prices
meta_close = meta['Close']
tesla_close = tesla['Close']

#Save data to file for later use if needed.
meta.to_csv('meta_stock_data.csv')
tesla.to_csv('tesla_stock_data.csv')

print("Stock data downloaded successfully.  Data saved to meta_stock_data.csv and tesla_stock_data.csv")
