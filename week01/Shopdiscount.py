def discount(price_items, discount_value):
    if price_items > 100:
        return price_items * discount_value
    else:
        return price_items
price_items = float(input("Enter the price of the item: "))
discount_value = 0.9
print(discount(price_items, discount_value))