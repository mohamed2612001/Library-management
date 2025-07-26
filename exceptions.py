class InvalidNumber(Exception):
    """check if number greater than zero and it type is integer"""

    ...


class BookNotFound(Exception):
    """check if book is in list of books"""

    ...


class InvalidRoughCorner(Exception):
    """check if string is digit or not"""

    ...


class InvalidID(Exception):
    """check is Id is composed of 4 digits"""

    ...


class NotStrongPassword(Exception):
    """check if password contains symbols and letters"""

    ...


class FillOut(Exception):
    """check all fields are filled out"""

    ...


class EmailError(Exception):
    """check if email is correct or not"""
    
    ...
