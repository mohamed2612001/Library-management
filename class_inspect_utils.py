import inspect


def get_attributes_types(cls) -> list:
    parms =inspect.signature(cls.__init__).parameters.values()
    return [parm.annotation for parm in parms if parm.annotation is not inspect._empty  ]


def get_attributes_names(cls) -> list[str]:
    parms = inspect.signature(cls.__init__).parameters
    return [name for name in parms if name != "self"]


def get_all_attributes(cls) -> dict:
    return dict(zip(get_attributes_names(cls),get_attributes_types(cls)))
