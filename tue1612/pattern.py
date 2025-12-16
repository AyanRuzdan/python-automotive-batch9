n = int(input("Enter triangle height: "))
if n > 0:
    for i in range(1, n+1):
        for j in range(i):
            print("*", end="")
        print()
