def repeat_add(a,b):
    product = 0
    for _ in range(int(b)):
        product += a
    return product

def repeat_sub(a, b):
    divide = 0
    if b == 0:
        print("Divide by zero not allowed")
        return None
    while a >= b:
        a -=b
        divide += 1
    return divide