import pyquant

Data = pyquant.Data(data_source="yfinance")
print(Data.adj_close_series('AAPL'))
