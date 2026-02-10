# item 1 price
item_1 = 162
# item 2 price
item_2 = 25
# $3 discount
discount_1 = 3
# item two price with discount_1 applied
item_2_discount = item_2 - discount_1
# purchased of item_1
purchase_item_1 = item_1 * 1.2
# subtotal variable
subtotal_price = purchase_item_1 + item_2_discount
# with .08 tax variable
tax = (purchase_item_1 + item_2_discount) * 0.08
# total price variable
total_price = tax + subtotal_price

print("Shopping Receipt")
print("-----------------------")
print("Item 1: $", purchase_item_1)  # Price per weight
print("Item 2: $", item_2_discount)  # Discounted price
print("-----------------------")
print("Subtotal: $", subtotal_price)
print("Tax (8%): $", tax)
print("-----------------------")
print("Thank you for shopping!")