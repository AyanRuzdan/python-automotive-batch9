print("Get min/max/swap value of variables")
print("1. Max\n2. Min\n3. Swap")
a, b = map(int, input("Enter a and b comma separated: ").split(','))
choice = int(input("Enter choice: "))
if choice == 1:
    print("Max of a and b is: ", max(a, b))
elif choice == 2:
    print("Min of a and b is: ", min(a, b))
elif choice == 3:
    a, b = b, a
    print("a and b after swap are: ", a, ", ", b)
else:
    print("Enter valid choice")
