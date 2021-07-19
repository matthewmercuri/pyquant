from typing import Union

from .data import Data


class Portfolio:

    def __init__(self, data_source: str, weights: False = bool) -> None:
        self.data = Data(data_source.upper().strip())
        self.portfolio = {}
        self.portfolio['positions'] = {}

    def _validate_ticker(self, ticker: str):
        return True

    def add_position(self, ticker: str, quantity: Union[float, int]):
        valid = self._validate_ticker()

        if valid:
            self.portfolio['positions'][ticker.upper().strip()] = quantity
        else:
            raise KeyError(f'{ticker} is not a valid symbol.')

    def update_position(self):
        pass

    def remove_position(self):
        pass

    def print_portfolio(self):
        print(self.portfolio)

    def historical_data(self):
        ''' returns pandas df of daily value '''

        positions = self.portfolio['positions']

        position_series = []
        for position in positions:
            _series = self.data.price_df(position)
            position_series.append(_series)
