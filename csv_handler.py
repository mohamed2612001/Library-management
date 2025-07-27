import csv

from validations import is_iterable
from class_inspect_utils import get_all_attributes

from typing import Any

def to_dict(objects: list | Any) -> list[dict] | dict:
    if isinstance(objects, list):
        return [object_to_dict(obj) for obj in objects]
    return object_to_dict(objects)


def object_to_dict(obj) -> dict:
    attrs: list[str] = get_attributes_names(type(obj))
    return {attr: getattr(obj, attr) for attr in attrs}


def read_csv_file(file) -> list[dict]:
    with open(file, mode="r", newline="") as f:
        csv_reader = csv.DictReader(f)
        data = list(csv_reader)
    return data


def write_csv_file(file, data: list[dict], field_names: list[str]) -> None:
    with open(file, mode="w", newline="") as f:
        csv_writer = csv.DictWriter(f, fieldnames=field_names)
        csv_writer.writeheader()
        csv_writer.writerows(data)


def add_objects_from_csv(cls, file):
    data = read_csv_file(file)
    for object in data:
        object = check_object(cls, object)
        values = list(object.values())
        cls(*values)


def check_object(cls, object: dict):
    attrs = get_all_attributes(cls)
    for key in object.keys():
        attr_data_type = attrs.get(key)
        if attr_data_type is int:
            object[key] = int(object[key])
        if attr_data_type is float:
            object[key] = float(object[key])
    return object
