import json

from csv_handler import to_dict

from typing import Any


def save_to_json(file_name: str, objects: list | dict, key="objects") -> None:
    if type(objects) != dict:
        objects = {key: to_dict(objects)}
    with open(file_name, "w") as f:
        json.dump(objects, f, indent=2)


def read_json_file(file_name: str) -> dict[list]:
    with open(file_name, "r") as f:
        data = json.load(f)
    return data


def add_object_to_json(file_name: str, objects: list | Any) -> None:
    json_data = read_json_file(file_name)
    dict_objects = to_dict(objects)
    key = list(json_data.keys())[0]
    if isinstance(dict_objects, dict):
        json_data[key].append(dict_objects)
    else:
        json_data[key].extend(dict_objects)
    save_to_json(file_name, json_data, key)
