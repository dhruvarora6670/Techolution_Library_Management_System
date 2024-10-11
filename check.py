from book import BookManager
from storage import Storage

class CheckoutManager:
    def __init__(self, storage_file='checkouts.csv'):
        self.checkouts = []
        self.book_manager = BookManager() # to interact with books
        self.storage_file = storage_file
        self.storage = Storage()
        self.headers = ['user_id', 'isbn']
        self.checkouts = self.load_checkouts()

    def checkout_book(self, user_id, isbn):
        result = self.book_manager.issue_book(isbn)
        if result == "Book issued successfully.":
            self.checkouts.append({"user_id": user_id, 'isbn': isbn})
            self.storage.save_data(self.storage_file, [{"user_id": user_id, 'isbn': isbn}], self.headers, append=True) # saving the book issueing records to csv
            return result
        else:
            return result
        
    def return_book(self, user_id, isbn):
        for checkout in self.checkouts:
            if checkout['user_id'] == user_id and checkout['isbn'] == isbn:
                self.book_manager.return_book(isbn) 
                self.checkouts.remove(checkout) 
                self.save_checkouts() # removing the book from checkedout / issued books (returning the book)
                return "Book returned successfully."
        return "No matching checout found."
    
    def save_checkouts(self):
        self.storage.save_data(self.storage_file, self.checkouts, self.headers, append=False)

    def load_checkouts(self):
        return self.storage.load_data(self.storage_file, self.headers)