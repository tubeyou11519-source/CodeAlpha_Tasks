STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 410,
    "AMZN": 185
}

def calculate_total(portfolio):
    total = 0
    for symbol, quantity in portfolio.items():
        price = STOCK_PRICES[symbol]
        total += price * quantity
    return total

def main():
    print("Stock Portfolio Tracker")
    print(f"Available stocks: {', '.join(STOCK_PRICES.keys())}\n")

    portfolio = {}

    while True:
        symbol = input("Enter stock symbol (or 'done' to finish): ").upper()
        if symbol == "DONE":
            break

        if symbol not in STOCK_PRICES:
            print("Unknown stock symbol. Try one from the list above.")
            continue

        quantity = int(input(f"Enter quantity of {symbol}: "))
        portfolio[symbol] = portfolio.get(symbol, 0) + quantity

    if not portfolio:
        print("No stocks entered. Exiting.")
        return

    print("\nYour Portfolio:")
    for symbol, quantity in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * quantity
        print(f"  {symbol}: {quantity} shares @ ${price} = ${value}")

    total = calculate_total(portfolio)
    print(f"\nTotal Investment Value: ${total}")

    save = input("\nSave this to a file? (y/n): ").lower()
    if save == "y":
        with open("portfolio_summary.txt", "w") as f:
            f.write("Stock Portfolio Summary\n")
            f.write("=" * 30 + "\n")
            for symbol, quantity in portfolio.items():
                price = STOCK_PRICES[symbol]
                value = price * quantity
                f.write(f"{symbol}: {quantity} shares @ ${price} = ${value}\n")
            f.write(f"\nTotal Investment Value: ${total}\n")
        print("Saved to portfolio_summary.txt")

if __name__ == "__main__":
    main()