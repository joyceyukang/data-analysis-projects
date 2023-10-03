import yfinance as yf
import pandas as pd
import json
import matplotlib

apple = yf.Ticker("AAPL")
print(apple)

with open('apple.json') as json_file:
    apple_info = json.load(json_file)
    # print the type of data variable
    # print((apple_info))
# print(apple_info['country'])
# apple_share_price_data = apple.history(period="max")
# (apple_share_price_data.head())
# apple_share_price_data.reset_index(inplace=True)
# (apple_share_price_data.plot(x="Date", y="Open"))
apple.dividends