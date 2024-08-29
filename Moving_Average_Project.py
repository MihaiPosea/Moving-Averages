import pandas as pd 
import datetime as dt
import matplotlib.pyplot as plt
import plotly.offline as pyo
import yfinance as yf

#Inputting Ticker Symbol
Ticker = input("Please Input ticker symbol in lowercase:")

#Create datetime information 
end = dt.datetime.now()
start = end - dt.timedelta(days=5000)

## Uses yfinance to get all stock information 
Stock = yf.Ticker(Ticker)
df = Stock.history(period="max")

## Fixes Date and makes it index
df.to_csv("{}.csv".format(Ticker))
df = pd.read_csv("{}.csv".format(Ticker))


#Moving Averages calculations
df["100 Day Moving Average"] = df["Close"].rolling(window = 100).mean() 
df["250 Day Moving Average"] = df["Close"].rolling(window = 250).mean() 

## Get the most recent moving average for both 100 days and 200 days.
MA_100_to_date = df["100 Day Moving Average"].iloc[-1]
MA_250_to_date = df["250 Day Moving Average"].iloc[-1]

##Function that returns investment advice
def Moving_Average_Investing(MA_100,MA_250):
     if MA_100 >= MA_250:
         print("Stock is on an upwards trajectory, signs are indicating to invest.")
     else:
         print("Stock is not on an upwards trajectory, signs are indicating to not invest")

Moving_Average_Investing(MA_100_to_date,MA_250_to_date)

## Plot information to get a better visual of it using plotly
pyo.init_notebook_mode(connected = True)
pd.options.plotting.backend = "plotly"
fig = make_subplots(rows = 2, cols = 1, shared_xaxes = True, vertical_spacing =0.1, subplot_titles = ("CBA", "Volume"), row_width = [0.2,0.7])
fig.add_trace(go.Candlestick(x=df.index, open = df["Open"], high = df["High"], low = df["Low"], close=df["Close"], name = "OHLC"))
fig.show()





















