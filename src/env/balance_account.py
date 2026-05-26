from datetime import datetime        
import pandas as pd
import plotly.graph_objects as go
from enum import Enum

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
