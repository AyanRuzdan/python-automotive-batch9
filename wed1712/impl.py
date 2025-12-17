import funcs

def calc():
    a, b = map(float, input("Enter two numbers comma sep: ").split(','))
    print("1. Add\n2.Diff\n3.Mult\n4.Divide")
    n = int(input("Enter choice: "))
    if n == 1:
        print(funcs.add(a, b))
    elif n == 2:
        print(funcs.sub(a, b))
    elif n == 3:
        print(funcs.mult(a, b))
    elif n == 4:
        print(funcs.divide(a, b))
    else:
        print("Please enter valid value")
