import yfinance as yf

ticker = yf.Ticker('MSFT')

print(ticker.info)