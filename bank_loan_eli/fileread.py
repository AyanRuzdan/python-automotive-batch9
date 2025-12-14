f = open('./bank_loan_eli/test_cases.txt','r')
f = f.read()
f = f.split('\n')
print(f)
f = f[1:]
print(f)
for vars in f:
    print(vars)
values = []
for row in f:
    values.append(row.split(','))
print(values)

for age,income,loan in values:
    print("age", age)
    print("income", income)
    print("loan", loan)