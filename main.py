from book import BookManager
from user import UserManager
from check import CheckoutManager

def main_menu():
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. List Books")
    print("3. Add User")
    print("4. Checkout Book")
    print("5. Return Book")
    print("6. Exit")
    choice = input("Enter choice: ")
    return choice

def main():
    book_manager = BookManager()
    user_manager = UserManager()
    checkout_manager = CheckoutManager()

    while True:
        choice = main_menu()
        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            print(book_manager.add_book(title, author, isbn))
        elif choice == '2':
            book_manager.list_books()
        elif choice == '3':
            name = input("Enter user name: ")
            user_id = input("Enter user ID: ")
            print(user_manager.add_user(name, user_id))
        elif choice == '4':
            user_id = input("Enter user ID: ")
            isbn = input("Enter ISBN of the book to checkout: ")
            print(checkout_manager.checkout_book(user_id, isbn))
        elif choice == '5':
            user_id = input("Enter user ID: ")
            isbn = input("Enter ISBN of the book to return: ")
            print(checkout_manager.return_book(user_id, isbn))
        elif choice == '6':
            print("Exiting.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()