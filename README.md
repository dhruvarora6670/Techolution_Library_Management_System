# Library Management System

## Description
The **Library Management System** is a command-line-based program that allows users to manage books, users, and book checkouts in a library. The system is built using Python and stores data in CSV files for books, users, and checkouts. This system provides functionality for adding books and users, issuing and returning books, and listing all the available books with their current status.

## Features
- **Add Book**: Add new books to the system with title, author, and ISBN.
- **List Books**: List all books with their details and issued status.
- **Add User**: Add users to the system with name and user ID.
- **Checkout Book**: Issue a book to a user.
- **Return Book**: Return a checked-out book.
- **Data Persistence**: Stores all book, user, and checkout data in CSV files.

## Files and Directories

### `main.py`
The main script that presents a menu to interact with the Library Management System. It provides options to add books, list books, add users, checkout books, return books, or exit the system.

### `book.py`
Handles all book-related operations, such as adding new books, listing available books, issuing books, and returning books. The issued status of each book is tracked and stored in a CSV file (`books.csv`).

### `user.py`
Manages user-related functionality, including adding new users and storing user information in a CSV file (`users.csv`).

### `check.py`
Handles the checkout and return of books. It interacts with the `BookManager` class to update book issued status and stores checkout details in a CSV file (`checkouts.csv`).

### `storage.py`
Provides utility functions for reading and writing data to and from CSV files. It ensures headers are written only once and supports both appending and overwriting data.

## CSV Files
- **`books.csv`**: Stores book details (`title`, `author`, `isbn`, `issued`) with `issued` marking whether the book is checked out.
- **`users.csv`**: Stores user information (`name`, `user_id`).
- **`checkouts.csv`**: Stores checkout details (`user_id`, `isbn`), tracking which user checked out which book.

## How to Run

1. **Clone the repository** or download the files.
2. Ensure that you have Python installed on your system.
3. Run the `main.py` script using Python:
   ```bash
   python main.py