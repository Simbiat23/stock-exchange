from rich import print
import requests as requests 
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Stock Market Dashboard")

stock_options = st.selectbox('Choose a stock', ['AAPL', 'MSFT', 'TSLA'])

api_key = "WUYIYQJYQDMWNQGH"
company = stock_options
url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock_options}&apikey={api_key}"
response = requests.get(url)
get_data = response.json()
df = pd.DataFrame(get_data ['Time Series (Daily)']).T
df = df.rename(columns={
    "1. open": "Open",
    "2. high": "High",
    "3. low": "Low",
    "4. close": "Close",
    "5. volume": "Volume"
})
df.index = pd.to_datetime(df.index)
df = df.astype(float)

st.subheader(f"{company} Closing Price (Last 100 Days)")
fig, ax = plt.subplots()
df["Close"].head(100).plot(ax=ax, title=f"{company} Closing Prices")
st.pyplot(fig)

# Show last 5 rows in a table
st.subheader("Latest Data")
st.dataframe(df.head())
