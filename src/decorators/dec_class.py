def autorepr(cls):
    """
    A decorator that adds a __repr__ method to a class, which returns a string
    representation of the instance, including all its attributes.
    """
    class_name = cls.__name__
    def __repr__(self):
        attr_strings = ", ".join(
            f"{name}={value!r}"
            for name, value in self.__dict__.items()
        )
        return f"{class_name}({attr_strings})"
    cls.__repr__ = __repr__
    return cls
