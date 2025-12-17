myset = {99, "apple", "banana", "pomegranate", "apple", True, 99, 2, False, 0}
print(myset)
empty_set = set()
empty_dict = {}
myset.add(10)
myset.discard(1)
print(myset)
mylist = [7, 8, 9]
myset.update(mylist)
for item in myset:
    print(item, end=" ")

# UNION OPERATOR PIPE SYMBOL
myset2 = {99, 98, 97}
print(myset | myset2)

# INTERSECTION use & AMPERSAND
print(myset & myset2)
