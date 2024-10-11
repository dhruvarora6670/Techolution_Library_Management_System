from storage import Storage

class Book:
    def __init__(self, title, author, isbn, issued=False):
        self._title = title
        self._author = author
        self._isbn = isbn
        self._issued = issued
    
    def get_details(self):
        return {
            "title": self._title,
            "author": self._author,
            "isbn": self._isbn,
            "issued": str(self._issued) # issued flag to make sure the book is not issued multiple times or returned without being issued
        }

class BookManager:
    def __init__(self, storage_file='books.csv'):
        self.storage_file = storage_file
        self.storage = Storage()
        self.headers = ['title', 'author', 'isbn', 'issued']
        self.books = self.load_books()
    
    def add_book(self, title, author, isbn):
        book = Book(title, author, isbn)
        self.books.append(book.get_details())
        self.storage.save_data(self.storage_file, [book.get_details()], self.headers, append=True) # adding new books
        return "Book added successfully."
    
    def list_books(self):
        self.books = self.load_books()
        for book in self.books:
            print(book)
    
    def issue_book(self, isbn):
        self.books = self.load_books()
        for book in self.books:
            if book['isbn'].strip().lower() == isbn.strip().lower(): # for case sentivity converted into lower case
                if book['issued'] == 'True':
                    return "This book is already issued."
                else:
                    book['issued'] = 'True' # marking the book as issued
                    self.save_books()
                    return "Book issued successfully."
        return "Book not found."

    def return_book(self, isbn):
        self.books = self.load_books()
        for book in self.books:
            if book['isbn'].strip().lower() == isbn.strip().lower(): # for case sentivity converted into lower case
                if book['issued'] == 'False':
                    return "This book is not currently issued."
                else:
                    book['issued'] = 'False' # marking the book as not issued
                    self.save_books()
                    return "Book returned successfully."
        return "Book not found."
    
    def save_books(self):
        self.storage.save_data(self.storage_file, self.books, self.headers, append=False)
    
    def load_books(self):
        return self.storage.load_data(self.storage_file, self.headers)