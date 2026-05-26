import gymnasium as gym
from datetime import datetime
import numpy as np
import yfinance as yf

from .state import PortfolioState, MarketState

class TradingEngine:
    def __init__(
            self, 
            granularity: str = 'M15', 
            initial_balance: float = 1000,
            starting_date: datetime = datetime(2022, 1, 1),
            ending_date: datetime = datetime(2022, 12, 31),
            ticker: str = 'AAPL',
        ):

        self.granularity = granularity
        self.ticker = ticker
        self.starting_date = starting_date
        self.ending_date = ending_date

        self.current_time = self.starting_date

        self.portfolio_state = PortfolioState(initial_balance)

    def step(self, action):
        pass

    def reset(self, initial_balance: float, granularity: float, price: float):
        pass

class TradingEnv(gym.Env):
    def __init__(self):
        super(TradingEnv, self).__init__()

    def step(self, action) -> ...:
        pass

    def reset(self):
        pass
    