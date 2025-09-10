from Order import Order

class User:
    def __init__(self, name):
        self.name = name
        self.order = Order()

    def checkout(self):
        total = self.order.calculate_total()
        print(f"{self.name}'s order total: ${total}")
