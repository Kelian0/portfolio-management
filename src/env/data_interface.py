from pydantic import BaseModel
from datetime import datetime



class Candle():
    def __init__(
        self,
        timestamp: str,
        open: float,
        high: float,
        low: float,
        close: float,
        ):

        self.timestamp = timestamp
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        

class Chart(list[Candle]):
    pass