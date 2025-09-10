from User import User   # ✅ Added import

class PremiumUser(User):
    def checkout(self):
        total = self.cart.calculate_total()
        discount = total * 0.10
        final_total = total - discount
        print(f"{self.name}'s cart total with 10% discount: ${final_total}")

