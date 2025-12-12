# Q. Print multiplication table 
n = int(input("Enter number: "))
print("The table of ", n)
for i in range(10):
    print(n, "*", i+1, "=", n*(i+1))
