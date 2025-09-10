from Course import Course
from Student import Student
from PremiumStudent import PremiumStudent

# Create courses
python = Course("Python Programming", "C101", 3, 400)
datasci = Course("Data Science 101", "C102", 3, 400)
ml = Course("Machine Learning", "C103", 3, 400)

# Create students
alice = Student("Alice")
bob = PremiumStudent("Bob")

# Alice enrolls
alice.enrollment.enroll_course(python)
alice.enrollment.enroll_course(datasci)
alice.enrollment.enroll_course(ml)
alice.enrollment.view_enrollment()
alice.checkout()

print("\n")

# Bob enrolls
bob.enrollment.enroll_course(python)
bob.enrollment.enroll_course(datasci)
bob.enrollment.enroll_course(ml)
bob.enrollment.view_enrollment()
bob.checkout()

print("\nDropping a course for Alice...")
alice.enrollment.drop_course(datasci)
alice.enrollment.view_enrollment()
alice.checkout()
