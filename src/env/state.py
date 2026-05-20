from dataclasses import dataclass
import numpy as np
import pandas as pd
from datetime import datetime 

import plotly.graph_objects as go

class PortfolioState:
    def __init__(self, initial_balance: float):
        self.balance = initial_balance
        self.balance_history = [initial_balance]

    def display(self):
        pass

class MarketState:
    def __init__(self, current_time: datetime, granularity: float, price: float):
        self.current_time = current_time
        self.granularity = granularity
        self.price = price

    def display(self):
        pass