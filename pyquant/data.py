from .yf import YF


class Data:
    def __init__(self, data_source: str) -> None:
        self.valid_data_sources = ['YFINANCE']

        if data_source not in self.valid_data_sources:
            raise KeyError(f'{data_source} is not a valid data source.')

        self.data = self._init_data_grabber(data_source)

    def _init_data_grabber(self, data_source: str):
        if data_source == 'YFINANCE':
            data_grabber = YF()

        return data_grabber

    def price_df(self, ticker: str, start_date=None, end_date=None):
        return self.data.price_df(ticker, start_date, end_date)

    def ticker_meta(self, ticker: str):
        '''
        returns a JSON like object holding meta data about the ticker:
        - name, industry, description,...
        '''
        pass
