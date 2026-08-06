"""
Question 4 - Shopping Bill

Ask:
- Customer name
- Number of items
- Product name
- Product price

Print:
====================
      RECEIPT
====================

Customer : John

Milk         ₹50.00
Bread        ₹35.00
Eggs        ₹120.00

--------------------
Total Amount : ₹205.00
====================

Thank you for shopping!
"""

# Customer Details
customer_name = input("Hello user, can you please enter your name? ").strip().title()
item_count = int(input("How many items did you buy? "))

# Store product details
product_names = []
prices = []
total = 0

# Get product information
for i in range(item_count):
    product_name = input(f"\nEnter Product {i + 1}: ").strip().title()
    product_names.append(product_name)

    price = float(input(f"Enter the price of {product_name}: ₹"))
    prices.append(price)

    total += price

# Print Receipt
print("\n====================")
print("      RECEIPT")
print("====================")

print(f"Customer : {customer_name}")
print(f"Items    : {item_count}")

print("\nProducts")
print("--------------------")

for i in range(item_count):
    print(f"{product_names[i]} : ₹{prices[i]:,.2f}")

print("--------------------")
print(f"Total Amount : ₹{total:,.2f}")
print("====================")

print("Thank you for shopping!")