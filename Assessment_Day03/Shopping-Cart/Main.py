from Product import Product
from User import User
from PremiumUser import PremiumUser

# Create products
laptop = Product("Laptop", 1000, 5)
mouse = Product("Mouse", 50, 10)

# Create users
alice = User("Alice")
bob = PremiumUser("Bob")

# Alice adds products
alice.cart.add_product(laptop, 1)
alice.cart.add_product(mouse, 2)

# Bob adds products
bob.cart.add_product(laptop, 1)
bob.cart.add_product(mouse, 3)

# View carts
print("\nAlice's Cart:")
alice.cart.view_cart()
alice.checkout()

print("\nBob's Cart:")
bob.cart.view_cart()
bob.checkout()

# Alice removes one product
alice.cart.remove_product(mouse)
print("\nAlice's Cart After Removing Mouse:")
alice.cart.view_cart()
alice.checkout()
