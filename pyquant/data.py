class Data:
    def __init__(self, data_source: str) -> None:
        self.valid_data_sources = ['YFINANCE']

        if data_source not in self.valid_data_sources:
            raise KeyError(f'{data_source} is not a valid data source.')

        self.data = self._init_data_grabber(data_source)

    def _init_data_grabber(self, data_source: str):
        if data_source == 'YFINANCE':
            pass

    def price_df(self, ticker):
        pass
