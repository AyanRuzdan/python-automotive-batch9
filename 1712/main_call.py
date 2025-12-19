import calculate
from funcs import pass_or_fail
a, b = map(float, input("Enter two numbers comma sep: ").split(','))
calculate.calc(a, b)


marks = list(map(int, input("Enter marks of 5 subjects: ").split()))

if pass_or_fail(marks):
    print("PASS")
else:
    print("FAIL")
