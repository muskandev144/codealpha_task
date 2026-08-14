def stock_tracker():
    # Hardcoded stock prices
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 140,
        "MSFT": 380,
        "AMZN": 170
    }
    
    print("=" * 50)
    print("STOCK PORTFOLIO TRACKER")
    print("=" * 50)
    print("Available stocks:", ", ".join(stock_prices.keys()))
    print()
    
    portfolio = {}
    total_investment = 0
    
    while True:
        stock = input("Enter stock name (or 'done' to finish): ").upper()
        
        if stock == "DONE":
            break
        
        if stock not in stock_prices:
            print("Stock not found! Try again.")
            continue
        
        try:
            quantity = int(input(f"Enter quantity for {stock}: "))
            if quantity < 0:
                print("Quantity cannot be negative!")
                continue
            
            investment = stock_prices[stock] * quantity
            portfolio[stock] = {
                "quantity": quantity,
                "price": stock_prices[stock],
                "total": investment
            }
            total_investment += investment
            print(f"Added {quantity} units of {stock}\n")
        
        except ValueError:
            print("Please enter a valid number!\n")
    
    if not portfolio:
        print("\nNo stocks added!")
        return
    
    # Display portfolio
    print("\n" + "=" * 50)
    print("YOUR PORTFOLIO")
    print("=" * 50)
    
    for stock, details in portfolio.items():
        print(f"{stock}: {details['quantity']} units @ ${details['price']} = ${details['total']}")
    
    print("-" * 50)
    print(f"Total Investment: ${total_investment}")
    print("=" * 50)
    
    # Save to file
    save = input("\nSave to file? (yes/no): ").lower()
    if save == "yes" or save == "y":
        with open("portfolio.txt", "w") as file:
            file.write("STOCK PORTFOLIO REPORT\n")
            file.write("=" * 50 + "\n\n")
            for stock, details in portfolio.items():
                file.write(f"{stock}: {details['quantity']} units @ ${details['price']} = ${details['total']}\n")
            file.write("-" * 50 + "\n")
            file.write(f"Total Investment: ${total_investment}\n")
        print("Portfolio saved to portfolio.txt!")

if __name__ == "__main__":
    stock_tracker()
