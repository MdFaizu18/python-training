class Member:
    def __init__(self, member_id, name):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
        
    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)
            return True
        else:
            return False
    
    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            return True
        else:
            return False
