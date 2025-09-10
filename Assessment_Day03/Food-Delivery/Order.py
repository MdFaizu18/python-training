class Order:
    def __init__(self):
        self.items = []
        self.last_ordered_item = None  

    def add_item(self, food_item):
        if food_item.available:
            self.items.append(food_item)
            self.last_ordered_item = food_item.name  
            print(f"Added '{food_item.name}' to order.")
        else:
            print(f"Sorry, {food_item.name} is not available.")

    def remove_item(self, food_item):
        if food_item in self.items:
            self.items.remove(food_item)
            print(f"Removed '{food_item.name}' from order.")
        else:
            print(f"{food_item.name} not found in order.")

    def view_order(self):
        if not self.items:
            print("Order is empty.")
        else:
            print("Order Items:")
            for item in self.items:
                print(f"- {item.name} = ${item.price}")

    def calculate_total(self):
        return sum(item.price for item in self.items)
