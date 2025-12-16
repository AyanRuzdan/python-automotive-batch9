# %s for strings and lists
myString = "python-automotive"
myList = [1, 3, 4, 5, 6, 7, 8, 9]
print("The string is %s and the list is %s" % (myString, myList))

# %d for integers
items = 14
cost = 13
total_cost = items * cost
print("The cost of %d items at rate %d is %d" % (items, cost, total_cost))

# %f for float
# cost is new updated
cost = 1.05*cost
total_cost = items * cost
print("The cost of %d items at rate %.2f is %.1f" % (items, cost, total_cost))

# %x and %X for hex values
num = 14
print("The hex of %d is %x / %X" % (num, num, num))
