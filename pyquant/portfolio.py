from .data import Data


class Portfolio:

    def __init__(self, data_source: str, weights: False = bool) -> None:
        self.data = Data(data_source.upper().strip())
        self.positions = []

    def add_positition(self):
        pass

    def update_position(self):
        pass

    def remove_position(self):
        pass
