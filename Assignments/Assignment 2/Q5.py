cost_price = float(input("Enter the cost price of the book: "))
discount = float(input("Enter the discount percentage: "))

discount_amount = (discount / 100) * cost_price
selling_price = cost_price - discount_amount

print(f"Discount Amount: {discount_amount}")
print(f"Selling Price of the Book: {selling_price}")
