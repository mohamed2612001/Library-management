import utils

import books_utils

from librarian import *


from book import *

librarian_menu = """
Librarian Options:
1. Change password
2. Add book
3. Remove book
4. Sell book
5. Search for a book
"""


def handle_librarian_flow():
    librarian: Librarian = check_get_user(Librarian.librarians)

    choice_of_librarian: int = utils.get_choice(librarian_menu, 5)

    if choice_of_librarian == 1:
        librarian.change_password()
    elif choice_of_librarian == 2:
        librarian.add_new_book()
    elif choice_of_librarian == 3:
        book: Book = books_utils.get_valid_book(search_with="name")
        Book.remove_book(book.name)
    elif choice_of_librarian == 4:
        books_utils.process_book_sales()
    else:
        books: Union[Book, list[Book]] = books_utils.get_books_by_search()
        Book.display_books(books)
