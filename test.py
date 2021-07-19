from pyquant import portfolio

print('hello')
Portfolio = portfolio.Portfolio('yfinance')
Portfolio.add_position('AAPL', 5)
Portfolio.print_portfolio()
Portfolio.historical_data()
