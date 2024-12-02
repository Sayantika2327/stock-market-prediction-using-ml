import numpy as np
import pandas as pd
import yfinance as yf
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

st.header('Stock Market Predictor')

# Input for stock symbol
stock = st.text_input('Enter Stock Symbol')
start = '2012-01-01'
end = '2024-12-31'

# Download stock data
if stock:
    data = yf.download(stock, start, end)

    st.subheader('Stock Data')
    st.write(data)

    # Moving averages
    ma_50_days = data['Close'].rolling(50).mean()
    ma_100_days = data['Close'].rolling(100).mean()
    ma_200_days = data['Close'].rolling(200).mean()

    # Price vs MA50
    st.subheader('Price vs MA50')
    fig1 = plt.figure(figsize=(8, 6))
    plt.plot(data['Close'], 'g', label='Close Price')
    plt.plot(ma_50_days, 'r', label='MA50')
    plt.legend()
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Price vs MA50')
    st.pyplot(fig1)

    # Price vs MA50 vs MA100
    st.subheader('Price vs MA50 vs MA100')
    fig2 = plt.figure(figsize=(8, 6))
    plt.plot(data['Close'], 'g', label='Close Price')
    plt.plot(ma_50_days, 'r', label='MA50')
    plt.plot(ma_100_days, 'b', label='MA100')
    plt.legend()
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Price vs MA50 vs MA100')
    st.pyplot(fig2)

    # Price vs MA100 vs MA200
    st.subheader('Price vs MA100 vs MA200')
    fig3 = plt.figure(figsize=(8, 6))
    plt.plot(data['Close'], 'g', label='Close Price')
    plt.plot(ma_100_days, 'r', label='MA100')
    plt.plot(ma_200_days, 'b', label='MA200')
    plt.legend()
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Price vs MA100 vs MA200')
    st.pyplot(fig3)
