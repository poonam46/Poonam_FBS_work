cost_price = int(input("Enter the cost price of item : "))
sell_price = int(input("Enter the selling price of item :"))

if(sell_price > cost_price):
    profit = sell_price - cost_price
    print("Profit = ",profit)
else:
    loss = cost_price - sell_price
    print("Loss = ",loss)