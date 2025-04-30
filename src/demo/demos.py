INITIAL = object()


def min(iterable, default=INITIAL):
    """Imperfect re-implementation of Python's built-in min function."""
    minimum = INITIAL
    for item in iterable:
        if minimum is INITIAL or item < minimum:
            minimum = item
    if minimum is not INITIAL:
        return minimum
    elif default is not INITIAL:
        return default
    else:
        raise ValueError("Empty iterable")
    


if __name__ == "__main__":
    # Test cases
    print(min([3, 1, 4, 1, 5, 9]))
    print(min([3, 1, 4, 1, 5, 9], default=0))
    print(min([], default=0))
    print(min([], default=INITIAL))