def repeat_add(a,b):
    product = 0
    for i in range(b):
        product += a
    return product

def repeat_subtract(a,b):
    divide  = 0
    while a>=b:
        a -= b
        divide += 1
    return divide

print(repeat_add(2,9))

print(repeat_subtract(18,3))