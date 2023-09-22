import yfinance as yf
import pandas as pd
import json

apple = yf.Ticker("AAPL")

with open('apple.json') as json_file:
    apple_info = json.load(json_file)
    # print the type of data variable
    print((apple_info))
# apple_info