from rich import print
import requests as requests 
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Stock Market Dashboard")
api_key = "WUYIYQJYQDMWNQGH"
default_ticker = "AAPL"

symbol = default_ticker

with st.form("search_company"):
    #search input 
    company_name = st.text_input("Enter company's ticker symbol(e.g AAPL)")
    search_button = st.form_submit_button(label="Search")
if search_button:
    if company_name:  
        symbol = company_name.upper()  
    else:
        symbol = default_ticker  

st.write(f"📌 Currently showing: **{symbol}**")

        
url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"
response = requests.get(url)
get_data = response.json() 
    
if "Time Series (Daily)" not in get_data:
        st.error("❌ Could not fetch data. Check the symbol or try again later.")
else:
    df = pd.DataFrame(get_data ['Time Series (Daily)']).T
    df = df.rename(columns={
    "1. open": "Open",
    "2. high": "High",
    "3. low": "Low",
    "4. close": "Close",
    "5. volume": "Volume"})
    df.index = pd.to_datetime(df.index)
    df = df.astype(float)

    st.subheader(f"{symbol} Closing Price (Last 100 Days)")
    fig, ax = plt.subplots() 
    df["Close"].head(100).plot(ax=ax, title=f"{symbol} Closing Prices")
    st.pyplot(fig)

        # Show last 5 rows in a table
    st.subheader("Latest Data")
    st.dataframe(df.head())

        
        
        
            

    # url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock_options}&apikey={api_key}"
      
   
    

# stock_options = st.selectbox('Choose a stock', ['AAPL', 'MSFT', 'TSLA'])

# api_key = "WUYIYQJYQDMWNQGH"
# # company = stock_options
# url = f"https://www.alphavantage.co/query?function=SYMBOL_SEARCH&symbol={company_name}&apikey={api_key}"
# # url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock_options}&apikey={api_key}"
# response = requests.get(url)
# get_data = response.json()


