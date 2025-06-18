# filename: install_and_plot.py
import subprocess
import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
from alpha_vantage.timeseries import TimeSeries


def install_packages():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"]) # upgrade pip first
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pandas", "matplotlib", "alpha-vantage"])
        print("Packages installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing packages: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred during installation: {e}")
        sys.exit(1)


def fetch_and_save_data(api_key):
    try:
        ts = TimeSeries(key=api_key, output_format='pandas')
        data_meta, meta_meta = ts.get_daily(symbol='META', outputsize='full')
        data_tesla, meta_tesla = ts.get_daily(symbol='TSLA', outputsize='full')

        data_meta['symbol'] = 'META'
        data_tesla['symbol'] = 'TSLA'
        combined_data = pd.concat([data_meta, data_tesla])
        combined_data.to_csv('stock_data.csv', index=True)
        print("Stock data downloaded successfully and saved to stock_data.csv")
    except Exception as e:
        print(f"Error fetching stock data: {e}")
        sys.exit(1)



def plot_data():
    try:
        df = pd.read_csv('stock_data.csv', index_col='timestamp', parse_dates=True)
        df = df.sort_index()

        plt.figure(figsize=(12, 6))
        for symbol in df['symbol'].unique():
            symbol_data = df[df['symbol'] == symbol]
            plt.plot(symbol_data.index, symbol_data['close'], label=symbol)

        plt.xlabel('Date')
        plt.ylabel('Closing Price')
        plt.title('META and TSLA Stock Price Change')
        plt.legend()
        plt.grid(True)
        plt.savefig('stock_price_chart.png')
        print("Chart created successfully and saved as stock_price_chart.png")

    except FileNotFoundError:
        print("Error: stock_data.csv not found. Please ensure data is fetched successfully.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred during plotting: {e}")
        sys.exit(1)


if __name__ == "__main__":
    api_key = "YOUR_API_KEY" # Replace with your Alpha Vantage API key
    install_packages()
    fetch_and_save_data(api_key)
    plot_data()