from book import *

from user import *

from csv_handler import add_objects_from_csv

class Librarian(User):
    TAX = 0.1

    librarians = []

    def __init__( self,  name: str = "",
        ID: str = "",
        address: str = "",
        password: str = "",
        email: str = "",
        hour_rate: int = 20,
        hours_work: int = 8):
        super().__init__(name, ID, address, password, email)
        self.__hour_rate = hour_rate
        self.__hours_work = hours_work
        self.salary_per_day = self.calculate_net_salary_per_day()
        Librarian.librarians.append(self)

    @property
    def hour_rate(self):
        return self.__hour_rate

    @hour_rate.setter
    def hour_rate(self, new_hour_rate):
        if is_valid_number(new_hour_rate):
            self.__hour_rate = new_hour_rate

    @property
    def hours_work(self):
        return self.__hours_work

    @hours_work.setter
    def hours_work(self, new_hours_work):
        if is_valid_number(new_hours_work):
            self.__hours_work = new_hours_work

    def __repr__(self):
        return (
            super().__repr__()
            + f"hour_rate:{self.hour_rate} hours_work:{self.hours_work}"
        )

    def calculate_net_salary_per_day(self) -> float:
        gross_salary = self.hours_work * self.hour_rate
        deduction = gross_salary * Librarian.TAX
        return gross_salary - deduction

    @staticmethod
    def add_new_book() -> None:
        Book.enter_details_of_books()

    @staticmethod
    def remove_book(name_book: str) -> None:
        book = Book.get_book_by_name(name_book)
        if book:
            Book.books.remove(book)
        else:
            print("this book not found to delete")

    @classmethod
    def add_books_from_csv(cls, file):
        add_objects_from_csv(cls, file)
