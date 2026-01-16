import yfinance as yf
import pandas as pd
import json
import requests
import matplotlib.pyplot as plt
# Using the Ticker module we can create an object that will allow us to access functions to extract data. 
# To do this we need to provide the ticker symbol for the stock, here the company is Apple and the ticker symbol is AAPL.



# url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/apple.json"
# response = requests.get(url)

# with open("apple.json", "w") as f:
#     f.write(response.text)


apple = yf.Ticker("AAPL")


with open ('apple.json') as jsonfile:
    apple_info = json.load(jsonfile)

# print(apple_info['country']) #United states

# share price of apple over certain time using history

# period="1d": Download 1 day of historical data.
# period="5d": Download 5 days of historical data.
# period="1mo": Download 1 month of historical data.
# period="3mo": Download 3 months of historical data.
# period="6mo": Download 6 months of historical data.
# period="1y": Download 1 year of historical data.
# period="2y": Download 2 years of historical data.
# period="5y": Download 5 years of historical data.
# period="10y": Download 10 years of historical data.
# period="ytd": Download historical data since the beginning of the current year.
# period="max": Download all available historical data.

apple_share_price_data = apple.history(period="max")
print(apple_share_price_data.head())
apple_share_price_data.reset_index(inplace=True)
# apple_share_price_data.plot(x="Date", y="Open")

# print(apple.dividends)
# plt.show()

# printing first row volume cell
i
print(apple_share_price_data.iloc[0]['Volume'])