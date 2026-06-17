''' Investment portfolio Analyzer  - an app designed to take csv based data of buy / sell orders for a portfolio.
Then process the data to provide  a breakdown of transactions, performance over time ,  AML style transaction flagging,
 along with GUI interface and graph plotting of performance over time.
Author - Christopher McPartland 16.06.2026'''


from Data_loader import *
from Calculations import *

portfolio_data = load_transactions("../data/trading_data.csv")
prices = market_indexes("../data/prices.csv")

print(len(portfolio_data))
print(prices)

current_portfolio_value = current_holdings(portfolio_data)
print(current_portfolio_value)