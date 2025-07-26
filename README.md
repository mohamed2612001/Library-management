# Library-management
## Library Management System
A simple Python-based library management system that supports:

Registration of members and librarians

Book management (add, remove, search)

Book purchasing and invoice display

Reading data from CSV files

## Project Structure
book.py – Contains the Book class for managing book data

user.py – Base User class

member.py – Member class (inherits from User) that handles book purchases

librarian.py – Librarian class (inherits from User) with permissions to manage books

utils.py, validations.py, class_inspect_utils.py – Utility and validation functions

csv_handler.py – Handles importing and exporting data from/to CSV files

books_utils.py, user_flow.py, librarian_flow.py – Business logic and user interaction flow

main.py – Entry point to choose the user type and run the program

