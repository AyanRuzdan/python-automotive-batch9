try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(result)
except ZeroDivisionError:
    print("The divisor cannot be zero")
except ValueError:
    print("Give numeric values only")
finally:
    print("Division done")
