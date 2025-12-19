def add(a, b):
    return a+b


def sub(a, b):
    return a - b


def mult(a, b):
    return a*b


def divide(a, b):
    if b == 0:
        print("Cannot divide by zero")
        return None
    return a/b


def pass_or_fail(marks):
    for mark in marks:
        if mark < 60:
            return False
    return True
