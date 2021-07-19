from .data import Data


class Portfolio:

    def __init__(self, data_source: str) -> None:
        self.data = Data(data_source.upper().strip())
