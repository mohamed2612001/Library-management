import datetime

from typing import Union

from validations import *


LIMITED_TRIES = 3


def get_current_date() -> str:
    current_date = datetime.datetime.today()
    return current_date.strftime("%d/%m/%Y, %H:%M:%S")


def get_values(cls_name, attributes: iter) -> list:
    all_values = []
    for attr_name, attr_type in attributes.items():
        prompt = f"please enter {attr_name}: "
        value = get_valid_input(cls_name, prompt, attr_name, attr_type)
        all_values.append(value)
    return all_values


def get_valid_input(
    cls_name, prompt: str, attr_name: str, attr_type
) -> Union[str, int]:
    while True:
        try:
            value = input(prompt)
            if attr_type is int:
                value = int(value)
            elif attr_type is float:
                value = float(value)
            dummy = cls_name.__new__(cls_name)
            setattr(dummy, attr_name, value)
            return value
        except Exception as e:
            print("Error:", e)
            print("try again")

def get_new_password(cls_name) -> str:
    prompt = "please enter new password"
    new_password = get_valid_input(cls_name, prompt, "password")
    return new_password

def check_old_password(current_password: str) -> bool:
    number_of_tries = 1
    while number_of_tries <= LIMITED_TRIES:
        print(current_password)
        old_password = input("please enter old password")
        if current_password == old_password:
            return True
        print("wrong password Try again")
        number_of_tries += 1
    print("you beyond the the limited of tries\n try at another time")
    return False





def get_correct_email_password(objects: list) -> tuple[str]:
    while True:
        email = input("enter your email: ")
        password = input("enter your password: ")
        if is_email_exists(objects, email) and is_password_exists(objects, password):
            return (email, password)
        print("please this email or password not correct\nTry again")


def get_yes_no(prompt: str) -> str:
    while True:
        answer = input(prompt + "enter (y) or (n): ").strip().lower()
        if answer == "y" or answer == "n":
            return answer
        print("please enter (y) for yes or (n) for No")


def get_choice(choices: Union[list, str], max_choice: int) -> int:
    while True:
        print(choices)
        try:
            choice = int(input(f"enter your choice from 1 to {max_choice} : ").strip())
            if 0 < choice <= max_choice:
                return choice
            print(f"please enter your choice from 1 to {max_choice}")
        except:
            print("please enter your choice in digit")


def check_get_user(users: list):
    email, password = get_correct_email_password(users)
    user = get_object_by_email(users, email)
    return user


def get_object_by_email(objects: list, email: str):
    return [obj for obj in objects if obj.email == email][0]