from User import User

class PremiumUser(User):
    def checkout(self):
        total = self.order.calculate_total()
        discount = total * 0.15
        final_total = total - discount
        print(f"{self.name}'s order total with 15% discount: ${final_total}")
