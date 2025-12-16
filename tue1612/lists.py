# list operations and outputs
mylist = [14, 1, 3, 1, 5, 7, 9]
print("Mylist\n", mylist)
mylist.append(-99)
print("Append -99\n", mylist)
mylist.remove(1)
print("Removed first occurence of 1\n", mylist)
mylist.pop()
print("Popped last element\n", mylist)
mylist.pop(2)
print("Popped index 2\n", mylist)
mylist.insert(3, 144)
print("Inserted 144 at index 3\n", mylist)
mylist.sort()
print("Sorted list\n", mylist)
mylist.clear()
print("List cleared\n", mylist)

# list comprehension using two lists
nums = [1, 2, 3, 4]
cubes = [x**3 for x in nums]
print("Cubes:", cubes)

# list comprehension using conditionals
nums.extend([6, 7, 8, 9])
print(nums)
even_cubes = [x**3 for x in nums if x % 2 == 0]
print("Even cubes:", even_cubes)
