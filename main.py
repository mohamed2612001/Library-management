from member import Member

from librarian import *

from book import *

from utils import get_choice

from csv_handler import add_objects_from_csv

from user_flow import handle_user_flow

from librarian_flow import handle_librarian_flow


add_objects_from_csv(Book, r"csv_books.csv")

add_objects_from_csv(Librarian, r"csv_librarians.csv")

add_objects_from_csv(Member, r"csv_members.csv")


user_type_menu = """
Select user type:
1. User
2. Librarian
"""


def main():
    choice = get_choice(user_type_menu, 2)
    if choice == 1:
        handle_user_flow()
    elif choice == 2:
        handle_librarian_flow()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
        exit()
