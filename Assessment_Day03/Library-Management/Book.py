class Book:
    def __init__(self,title,author,ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.is_available = True
        
    def borrow(self):
        if self.is_available:
            self.is_available = False
            return True
        else:
            return False
        
    def return_book(self):
        self.is_available = True
        
    def show_info(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.ISBN}, Available: {self.is_available}"
        
    def __str__(self):
        return self.show_info()
    