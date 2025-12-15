while True:
    name = input("Enter name: ")
    if name == "":
        break

for i in "123-456-7890":
    if i == "-":
        continue
    print(i, end="")
print()
for i in range(1, 21):
    if i == 13:
        pass
    print(i, end=" ")
