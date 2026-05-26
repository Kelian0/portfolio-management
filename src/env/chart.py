from datetime import datetime        
import pandas as pd
import plotly.graph_objects as go
from enum import Enum

class Chart:
    """
    Attributs:
        data: Pandas Dataframe contening OHLCV data with time as index
        granularity: 
        ticker: 
        starting_date: 
        ending_date: 
    """

    def __init__(
            self,
            data: pd.DataFrame,
            granularity: str = 'M15',
            ticker: str = 'AAPL',
            starting_date: datetime = datetime(2026, 4, 1),
            ending_date: datetime = datetime(2026, 4, 30),
            ):

        self.df_data = data
        self.granularity = granularity
        self.ticker = ticker
        self.starting_date = starting_date
        self.ending_date = ending_date

    def checker(self):
        """
        Check l'état du dataframe 
        """
        ...

    def plot(self):
        """
        Plot the chart using plotly
        """
        ...

    def to_df(self):
        ...

class BalanceAccount():
    """
    """
    def __init__(self, initial_balance: float):
        balance_history = [initial_balance]
        balance = initial_balance
    
    def add_profit(self, profit: float):
        self.balance += profit
        self.balance_history.append(self.balance)

    def add_loss(self, loss: float):
        """
        No very usefull, prefer using add_profit
        """
        self.balance -= loss
        self.balance_history.append(self.balance)

    def display(self):
        """
        Display the balance history using plotly
        """
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            y=self.balance_history,
            mode='lines',
            name='Account Balance'
        ))
        fig.update_layout(
            title='Account Balance History',
            xaxis_title='Steps',
            yaxis_title='Balance',
            template='plotly_dark'
        )
        fig.show()
