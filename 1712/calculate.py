from funcs import add, sub, mult, divide


def calc(a, b):

    while True:

        print("1. Add\n2.Diff\n3.Mult\n4.Divide\n5.Exit")
        n = int(input("Enter choice: "))

        if n == 1:
            print(add(a, b))
        elif n == 2:
            print(sub(a, b))
        elif n == 3:
            print(mult(a, b))
        elif n == 4:
            print(divide(a, b))
        elif n == 5:
            break
        else:
            print("Please enter valid value")
