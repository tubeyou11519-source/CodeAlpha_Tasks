# Stock Portfolio Tracker

A command-line tool that calculates the total value of a stock portfolio based on hardcoded stock prices.

## Features
- Uses a hardcoded dictionary of 5 stock symbols and their prices
- Lets the user enter multiple stocks with quantities
- Calculates and displays total investment value
- Optionally saves a summary to a text file

## How to Run
```
python tracker.py
```


## Concepts Used
- Dictionary: storing stock symbols and prices
- Input/output: reading user entries, printing the summary
- Basic arithmetic: calculating price × quantity for each stock
- File handling: optionally saving results to a .txt file

## Example
C:\User\CodeAlpha_StockPortfolioTracker>python tracker.py
Stock Portfolio Tracker
Available stocks: AAPL, TSLA, GOOGL, MSFT, AMZN

Enter stock symbol (or 'done' to finish): amzn
Enter quantity of AMZN: 7
Enter stock symbol (or 'done' to finish): tsla
Enter quantity of TSLA: 12
Enter stock symbol (or 'done' to finish): googl
Enter quantity of GOOGL: 9
Enter stock symbol (or 'done' to finish): done

Your Portfolio:
  AMZN: 7 shares @ $185 = $1295
  TSLA: 12 shares @ $250 = $3000
  GOOGL: 9 shares @ $140 = $1260

Total Investment Value: $5555
Save this to a file? (y/n): y
Saved to portfolio_summary.txt