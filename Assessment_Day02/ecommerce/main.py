import cart, payment

cart.add_item("Shoes", 2000)
cart.add_item("Bag", 1500)
print("Cart Total:", cart.total())
print(payment.process_payment(cart.total()))


cart.remove_item("Shoes")
print("Cart after removal:", cart.cart)
print("Total:", cart.total())

