mytup = (1, 2, "Ayan", 1, 1, 2, 2, 2, 21)
print(mytup[0])
print(mytup.count(2))
print(mytup.index("Ayan"))

for item in mytup:
    print(item, end=", ")

ll = [(x, str(x+2)) for x in range(4)]
for k, v in ll:
    print("\n%d:%s:%s" % (k, v, type(v)), end=" ")
