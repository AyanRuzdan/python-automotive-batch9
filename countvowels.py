s = input()
vowels = "aeiou"
count = 0
for c in s:
    if c.lower() in vowels:
        count += 1
print(count)
