class Cart:
    def __init__(self):
        self.items = []   

    def add_product(self, product, quantity):
        if product.stock >= quantity:
            self.items.append((product, quantity))
            product.stock -= quantity  
            print(f"Added {quantity} x {product.name} to cart.")
        else:
            print(f"Sorry, not enough stock for {product.name}.")

    def remove_product(self, product):
        for item in self.items:
            if item[0] == product:
                self.items.remove(item)
                product.stock += item[1]  
                print(f"Removed {product.name} from cart.")
                return
        print(f"{product.name} not found in cart.")

    def view_cart(self):
        if not self.items:
            print("Cart is empty.")
        else:
            print("Cart Items:")
            for product, qty in self.items:
                print(f"- {product.name} x {qty} = ${product.price * qty}")

    def calculate_total(self):
        return sum(product.price * qty for product, qty in self.items)
