# list of strings
stringlist = ["a", "aa", "bbb"]

# list of integers
numlist = [1, 2, 3]

# make 2d-list using previous lists
mat = [stringlist, numlist]
# print(stringlist, numlist, mat, sep="\n")

# access entire list
print(mat)

# access zeroeth list in 2d-list
print(mat[0])

# access oneth element in zeroeth sublist
print(mat[0][1])

# multiply list
print(mat[0]*2)
print(mat[1]*2)

# plus operator
print(mat[0]+mat[1])
