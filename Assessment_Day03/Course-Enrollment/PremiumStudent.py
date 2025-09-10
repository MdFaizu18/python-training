from Student import Student

class PremiumStudent(Student):
    def checkout(self):
        credits = self.enrollment.calculate_credits()
        fees = self.enrollment.calculate_fees()
        discount = fees * 0.20
        final_fees = fees - discount
        print(f"{self.name}'s total credits: {credits}, Fees with discount: ${final_fees}")
