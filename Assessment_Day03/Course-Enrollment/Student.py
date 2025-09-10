from Enrollment import Enrollment

class Student:
    def __init__(self, name):
        self.name = name
        self.enrollment = Enrollment()

    def checkout(self):
        credits = self.enrollment.calculate_credits()
        fees = self.enrollment.calculate_fees()
        print(f"{self.name}'s total credits: {credits}, Fees: ${fees}")
