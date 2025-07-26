from exceptions import *

from utils import *

from validations import *

from csv_handler import add_objects_from_csv

from class_inspect_utils import get_all_attributes
class Book:

    books = []

    def __init__(
        self,
        name: str,
        author: str,
        quantity: int,
        price: float,
        genre: str,
        corner: str,
        rough: str,
    ):
        self.__name = name.strip().title()
        self.__author = author.strip().title()
        self.__quantity = int(quantity)
        self.__price = float(price)
        self.__corner = corner.strip()
        self.__rough = rough.strip()
        self.__Type = genre.strip().title()
        Book.books.append(self)

    def __str__(self):
        return f"{self.name} the author:{self.author} there are {self.quantity} of this book"

    def __repr__(self):
        return f"({self.__class__.__name__ }\
            name:{self.name}\
            author:{self.author}\
            quantity:{self.quantity}\
            rough:{self.rough}\
            corner:{self.corner}\
            genre:{self.genre}"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if is_fill_out(new_name):
            self.__name = new_name

    @property
    def genre(self):
        return self.__Type

    @genre.setter
    def genre(self, new_Type):
        if is_fill_out(new_Type):
            self.__Type = new_Type

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, new_author):
        if is_fill_out(new_author):
            self.__author = new_author

    @property
    def rough(self):
        return self.__rough

    @rough.setter
    def rough(self, new_rough):
        if is_valid_corner_rough(new_rough):
            self.__rough = new_rough

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if is_valid_number(new_price):
            self.__price = new_price

    @property
    def corner(self):
        return self.__corner

    @corner.setter
    def corner(self, new_corner):
        if is_valid_corner_rough(new_corner):
            self.__corner = new_corner

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, new_number):
        if is_valid_number(new_number):
            self.__quantity = new_number

    @classmethod
    def display_the_place_of_book(cls, name_of_book: str) -> None:
        book = cls.get_book_by_name(name_of_book)
        print(f"you can find this book in corner {book.corner} ,rough{book.rough}")

    @classmethod
    def get_book_by_name(cls, name_of_book: str) -> "Book":
        return (cls.is_book_in_list(name_of_book, name=True)[0])

    @classmethod
    def is_book_in_list(
        cls, book: str, author: bool = False, name: bool = False, genre: bool = False
    ) -> list["Book"]:
        book = book.strip().title()
        if author:
            element = [elem for elem in cls.books if elem.author == book]
        elif name:
            element = [elem for elem in cls.books if elem.name == book]
        elif type:
            element = [elem for elem in cls.books if elem.genre == book]

        if element:
            return element
        raise BookNotFound(f"this {book} not found in our library")

    @classmethod
    def display_books_using_type(cls, type_of_book: str) -> list["Book"]:
        books = cls.get_books_by_genre(type_of_book)
        cls.display_books(books=books)

    @classmethod
    def get_books_by_genre(cls, genre: str) -> list:
        return cls.is_book_in_list(genre, genre=True)

    @classmethod
    def display_books_using_author(cls, author: str) -> list["Book"]:
        books = cls.get_books_by_author(author)
        cls.display_books(books=books)

    @classmethod
    def get_books_by_author(cls, name_of_author: str) -> list:
        return cls.is_book_in_list(name_of_author, author=True)

    @classmethod
    def display_books(cls, books: list = None) -> list:
        if books == None:
            books = cls.books
        for i, book in enumerate(books, 1):
            print(f"{i}. {cls.display_book(book)} ")
            print("_" * 40)
        return books

    @staticmethod
    def display_book(book: "Book") -> str:
        if book.quantity == 0:
            return f"{book.name}\tWrite By : {book.author } it costs {book.price} (not avilable now)"
        return f"{book.name}\tWrite By : {book.author } it costs {book.price}"

    @classmethod
    def display_bought_books(cls, books) -> None:
        print(f"   {'Book':<20} {'Price':<10} {'Quantity':<10} {'Subtotal':<10}")
        print("-" * 50)
        for i, book in enumerate(books, 1):
            subtotal = book.price * book.quantity
            print(
                f"{i}. {book.name:<20} {book.price:<10.2f} {book.quantity:<10} {subtotal:<10.2f}"
            )

        print("-" * 50)
        print(f"{'Total Price:':<35} {cls.get_total_price(books):.2f}")

    @staticmethod
    def get_total_price(books: list["Book"]) -> float:
        sum = 0
        if len(books) != 1:
            for book in books:
                sum += book.price * book.quantity
            return sum
        return books[0].price * books[0].quantity


    @classmethod
    def enter_details_of_books(cls) -> None:
        all_attributes = get_all_attributes(cls)
        values = get_values(cls, all_attributes)
        cls(*values)

    @classmethod
    def remove_book(cls, name_book: str) -> None:
        book = cls.get_book_by_name(name_book)
        if book:
            cls.books.remove(book)
        else:
            print("this book not found to delete")

    @classmethod
    def add_books_from_csv(cls, file) -> None:
        add_objects_from_csv(cls, file)


