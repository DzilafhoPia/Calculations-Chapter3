"""create a simple self-checkout system. Prompt for the prices and quantities of 3 items, calculate the subtotal of the
items then calculate tax using  a tax rate of 5.5%"""
item1 = int(input("Enter the price of item 1: "))
quantity_item1 = int(input("Enter the quantity of item 1: "))
item2 = int(input("Enter the price of item 2: "))
quantity_item2 = int(input("Enter the quantity of item 2: "))
item3 = int(input("Enter the price of item 3: "))
quantity_item3 = int(input("Enter the quantity of item 3: "))
subtotal1 = ((item1 * quantity_item1) + (item2 * quantity_item2) + (item3 * quantity_item3))
subtotal = "{:.2f}".format(subtotal1)
print(f"Subtotal: ${subtotal}")
Tax = (5.5 * float(subtotal)) / 100
print(f"Tax: ${Tax}")
Total = (float(subtotal) + float(Tax))
print(f"Total: ${Total}")