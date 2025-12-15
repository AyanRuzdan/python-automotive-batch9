n = int(input())
flag = True

if n < 2:
    print("Not prime")
else:
    for i in range(2, n):
        if n% i == 0:
            flag = False
            break

if flag == True:
    print("Prime")
else:
    print("Not Prime")