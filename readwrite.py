# # Q. Read write from file

# use the with open function and read from file
print("Original content of file.txt")
with open("file.txt", "r") as f:
    print(f.read())

# write into the file using "write" mode
with open("file.txt", "w") as f:
    f.write("Hello, this is new text.\nNew line text")

print("\nAfter overwriting")
# read the file again to check what is written
with open("file.txt", "r") as f:
    print(f.read())


## Secondary approach
# f = open("file.txt", "r+")
# print(f.read())
# f.write("\nThis is a new line")
# print(f.read())
# f.close()
