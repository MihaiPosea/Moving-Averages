Overview
This script analyzes a stock's moving averages using historical data from Yahoo Finance (yfinance). It calculates the 100-day and 250-day moving averages and provides investment advice based on their comparison. The script also visualizes the stock's price movements using Plotly.

Requirements
You'll need the following Python libraries:

pandas
datetime
matplotlib
plotly
yfinance

Usage
Input the stock symbol: Enter the ticker symbol of the stock in lowercase.
Data Fetching: The script retrieves the stock's historical data for up to 5000 days.
Moving Averages Calculation:
100-Day Moving Average: Calculated as the rolling average of the stock's closing prices over the last 100 days.
250-Day Moving Average: Calculated as the rolling average of the stock's closing prices over the last 250 days.

Investment Advice:
The script compares the most recent 100-day and 250-day moving averages.
Advice: If the 100-day moving average is greater than or equal to the 250-day moving average, the script suggests that the stock is on an upward trajectory and may be a good investment.

Visualization:
A candlestick chart of the stock's price movements is plotted using Plotly.

Outputs:
Investment Advice: Based on the comparison of the 100-day and 250-day moving averages.
Plot: Candlestick chart showing the stock's price movements.
