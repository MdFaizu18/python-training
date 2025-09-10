from Book import Book
from Member import Member

b1 = Book("Python Basics", "Alice", "1234567890")
b2 = Book("Learning OOP", "Bob", "0987654321")

m1 = Member("123", "Faiz")

print("Before Borrowing books...")
print(b1)
print(b2)


print("\nBorrowing books...")
m1.borrow_book(b1)
m1.borrow_book(b2)

print(b1)
print(b2)

print("\nReturning one book...")
m1.return_book(b1)

print(b1)
print(b2)
