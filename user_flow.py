import utils

import books_utils

from book import *

from member import *

continue_shopping_menu = """
1. Continue shopping
2. Stop shopping
"""

user_menu = """
User Options:
1. Change password
2. Buy book from library
3. Buy book online
"""

def handle_user_flow() -> None:
    answer = utils.get_yes_no("are you have an account")
    if answer == "y":
        user = utils.check_get_user(Member.members)
    else:
        user = Member()
    choice_user_menu = utils.get_choice(user_menu, 3)
    if choice_user_menu == 1:
        user.change_password()
    else:
        user_shop_flow(user,choice_user_menu)

def user_shop_flow(user: "Member", choice_user_menu: int) -> None:
    while True:

        books = books_utils.get_books_by_search()
        book = books_utils.get_book(books)
        if choice_user_menu == 2:
            book.display_the_place_of_book(book.name)
        elif choice_user_menu == 3:
            skip_book = books_utils.process_book_selection(book,user.books_bought)
            if skip_book == 0:
                continue
         
        choice_of_continue = utils.get_choice(continue_shopping_menu, 2)
        if choice_of_continue == 1:
            continue
        if choice_user_menu == 3:
            Book.display_bought_books(user.books_bought)
            user.add_transactions()
        print("thank you for visiting our library")
        break