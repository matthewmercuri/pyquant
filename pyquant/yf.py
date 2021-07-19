import yfinance as yf


class YF:
    def __init__(self) -> None:
        pass

    def price_df(self, ticker: str, start_date, end_date):
        if start_date is None and end_date is None:
            df = yf.Ticker(ticker, period='max')
        else:
            raise NotImplementedError('This is an upcoming feature')

        return df
