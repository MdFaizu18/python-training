class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def display(self):
        return f"{self.name} - Price: ${self.price}, Stock: {self.stock}"
