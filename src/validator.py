def is_number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def is_positive(value):
    return is_number(value) and value > 0