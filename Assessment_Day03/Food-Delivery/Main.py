from FoodItem import FoodItem
from User import User
from Premiumuser import PremiumUser

# Create food items
pizza = FoodItem("Pizza", 300)
burger = FoodItem("Burger", 200)
pasta = FoodItem("Pasta", 250, available=False)  

# Create users
john = User("John")
emma = PremiumUser("Emma")

# John orders food
john.order.add_item(pizza)
john.order.add_item(burger)
john.order.add_item(pasta)  
john.order.view_order()
john.checkout()

print("\n")

# Ema orders food
emma.order.add_item(pizza)
emma.order.add_item(burger)
emma.order.view_order()
emma.checkout()

# Remove item
john.order.remove_item(burger)
print("\nAfter removing Burger:")
john.order.view_order()
john.checkout()

