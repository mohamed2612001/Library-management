from typing import Literal,Union

from re import findall

from exceptions import *

from string import ascii_letters, punctuation

from collections.abc import Iterable


def is_valid_corner_rough(new_value: str) -> Literal[True]:
    if isinstance(new_value, str) and new_value.isdigit():

        return True
    raise InvalidRoughCorner("please enter the rough or corner in digit")


def is_valid_number(number: Union[int,float]) -> Literal[True]:
    if (isinstance(number, int) or isinstance(number,float) )and number >= 0:
        return True
    raise InvalidNumber(
        f"you should type number in positive and its type should be int"
    )


def is_password_strong(password: str) -> Literal[True]:
    check_punctuation = [True for letter in password if letter in punctuation]
    check_letters = [True for letter in password if letter in ascii_letters]
    if all([check_punctuation, check_letters]):
        return True
    raise NotStrongPassword("your password should contain symobls and letters")


def is_fill_out(*args) -> Literal[True]:
    if all([field.strip() != "" for field in args]):
        return True
    raise FillOut("please fill out all fields")


def is_valid_ID(new_ID: str) -> Literal[True]:
    if isinstance(new_ID, str) and new_ID.isdigit() and len(new_ID) == 4:
        return True

    raise InvalidID("please type ID in digit and the ID should be 14 digits")


def is_iterable(elem: Iterable) -> bool:
    return isinstance(elem, Iterable)


def is_valid_email(email: str) -> str:
    email_pattern = r".+@.+\.com"
    if findall(email_pattern, email):
        return email
    raise EmailError("please your email not valid \n please check your email")

def is_email_exists(objects: list, email: str ) -> bool:
    for obj in objects:
        if obj.email == email:
            return True
    return False   

def is_password_exists(objects: list, password: str) -> bool:
    for obj in objects:
        if obj.password == password:
            return True
    return False


