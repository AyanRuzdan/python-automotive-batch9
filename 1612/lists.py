# list operations and outputs
mylist = [14, 1, 3, 1, 5, 7, 9]
print("Mylist\n", mylist)

# append to end of list
mylist.append(-99)
print("\nAppend -99\n", mylist)

# remove first occurrence
mylist.remove(1)
print("\nRemoved first occurence of 1\n", mylist)

# pop from end of list
mylist.pop()
print("\nPopped last element\n", mylist)

# pop index
mylist.pop(2)
print("\nPopped index 2\n", mylist)

# insert second value at given index
mylist.insert(3, 144)
print("\nInserted 144 at index 3\n", mylist)

# sort the list, do not reassign
mylist.sort()
print("\nSorted list\n", mylist)

# clear all elements and get empty list
mylist.clear()
print("\nList cleared\n", mylist)

# list comprehension using two lists
nums = [1, 2, 3, 4]
cubes = [x**3 for x in nums]
print("\nCubes:", cubes)

# list comprehension using conditionals
nums.extend([6, 7, 8, 9])
print(nums)
even_cubes = [x**3 for x in nums if x % 2 == 0]
print("\nEven cubes:", even_cubes)
keep_all = [x if x % 3 else -1 for x in nums]
print(keep_all)
