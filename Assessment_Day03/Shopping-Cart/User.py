from Cart import Cart   

class User:
    def __init__(self, name):
        self.name = name
        self.cart = Cart()

    def checkout(self):
        total = self.cart.calculate_total()
        print(f"{self.name}'s cart total: ${total}")
