from typing import Union

from book import *

from member import *

from copy import deepcopy

search_menu = """
Search by:
1. Name
2. Author
3. Genre/type
"""

book_quantity_handling_menu = (
    "Choose an option:\n"
    "1. Take all available books\n"
    "2. Enter quantity again\n"
    "3. Skip this book\n"
)


def process_book_selection(book: "Book", cart: list["Book"]):
    quantity = get_quantity(book)
    if quantity == 0:
        return 0  # refers to skip the book

    purchased_copy = assign_quantity_and_update_original(book, quantity)
    cart.append(purchased_copy)

    handle_delete_from_cart(cart)


def get_book(books: Union[list["Book"], "Book"]) -> "Book":
    if isinstance(books, list):
        Member.display_books(books)
        index_book = get_choice("", len(books)) - 1
        book = books[index_book]
    else:
        book = books
    return book


def get_books_by_search() -> Union[list["Book"], "Book"]:
    choice_of_search = get_choice(search_menu, 3)

    if choice_of_search == 1:
        books = get_valid_book(search_with="name")
    elif choice_of_search == 2:
        books = get_valid_book(search_with="author")
    else:
        books = get_valid_book(search_with="genre")

    return books


def handle_delete_from_cart(cart) -> None:
    Book.display_bought_books(cart)
    answer_to_delete = get_yes_no("DO you want to delete book from cart: ")
    if answer_to_delete == "y":
        index_deleted_book = (get_choice("", len(cart))) - 1
        confirm_book_deletion(index_deleted_book, cart)
    return None


def confirm_book_deletion(index_of_book: int, bought_books) -> None:
    deleted_book = bought_books[index_of_book]
    to_certain = get_yes_no(f"are you sure to delete {deleted_book.name}: ")
    if to_certain == "y":
        print(f"{deleted_book.name} deleted successfully")
        old_book = Book.get_book_by_name(deleted_book.name)
        old_book.quantity += deleted_book.quantity
        del bought_books[index_of_book]


def process_book_sales() -> None:
    cart = []
    while True:
        book = get_valid_book(search_with="name")
        quantity_of_book = get_quantity(book)
        if quantity_of_book != 0:
            copy_book = assign_quantity_and_update_original(book, quantity_of_book)
            cart.append(copy_book)
        answer = get_yes_no("Do you want to sell another book")
        if answer == "y":
            continue
        ans = handle_delete_from_cart(cart)
        if ans == None:
            Book.display_bought_books(cart)
            break
        
        
def assign_quantity_and_update_original(book: "Book", quantity) -> "Book":
    copy_book = deepcopy(book)
    copy_book.quantity = quantity
    book.quantity -= quantity
    return copy_book


def get_quantity(book: "Book") -> int:
    while True:
        number_of_book = int(input("enter the quantity of book: "))
        if 0 < number_of_book <= book.quantity:
            return number_of_book
        print(f"the available quantity of this book is {book.quantity}")
        choice_of_quantity = get_choice(book_quantity_handling_menu, 3)
        if choice_of_quantity == 1:
            return book.quantity
        elif choice_of_quantity == 2:
            continue
        return 0



def get_valid_book(search_with="name") -> list["Book"]:
    while True:
        try:
            book_name = input(f"enter the {search_with} of book: ")
            if search_with == "name":
                book = Book.is_book_in_list(book_name, name=True)[0]
            elif search_with == "author":
                book = Book.is_book_in_list(book_name, author=True)
            elif search_with == "genre":
                book = Book.is_book_in_list(book_name, genre=True)
            return book
        except BookNotFound as e:
            print(e)
            print(f"please enter correct {search_with} ")


