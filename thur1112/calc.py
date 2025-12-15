def calculate(a, b, op):
    if op == '+': return a + b
    elif op == '-': return a - b
    elif op == '*': return a * b
    elif op == '/': return a / b
    else: return "Invalid Operator"
a = float(input("Enter num1: "))
b = float(input("Enter num2: "))
op = input("Enter operator (+ - * /): ")
print(calculate(a, b, op))