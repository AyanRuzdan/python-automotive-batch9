class Library:
    def __init__(self, id, username, books=None):
        if books is None:
            books = []
        self.id = id
        self.username = username
        self.books = books

    def has_book(self, book_name):
        return book_name in self.books

    def borrow(self, book_name):
        if self.has_book(book_name):
            print(f"{book_name} already borrowed")
            return None
        else:
            self.books.append(book_name)
            print(f"{book_name} borrowed successfully")

    def return_book(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            print(f"{book_name} returned successfully")
        else:
            print(f"{book_name} not found in borrowed books")
            return None


mem1 = Library(1, "Ayon")
print(mem1.books)
mem1.borrow("1984")
print(mem1.books)
mem1.borrow("IQ84")
print(mem1.books)
mem1.borrow("IQ84")
mem1.return_book("Animal Farm")
print(mem1.books)
mem1.return_book("1984")
print(mem1.books)
