import streamlit as st, pandas as pd
import requests
from bs4 import BeautifulSoup
import time

st.header('Indian Stock Dashboard')

ticker = st.sidebar.text_input('Symbol Code', 'INFY')
exchange = st.sidebar.text_input('Exchange', 'NSE')

url = f'https://www.google.com/finance/quote/{ticker}:{exchange}'


response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
price = float(soup.find(class_='YMlKec fxKbKc').text.strip()[1:].replace(",", ""))
prev_close = float(soup.find(class_='P6K39c').text.strip()[1:].replace(",", ""))
revenue = soup.find(class_='QXDnM').text
news = soup.find(class_='Yfwt5').text
#about = soup.find(class_='bLLb2d').text

dict1 = {'Price' : price, 'Previous Close' : prev_close, 'Revenue' : revenue, 'News' : news}

df=pd.DataFrame(dict1, index=['Extracted Data']).T

st.write(df)

