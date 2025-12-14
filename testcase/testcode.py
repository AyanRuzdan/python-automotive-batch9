def check_eligibility(age,income,loan):
    if age <=0 or income <0 or loan<0:
        return "Invalid Input"
    elif age <21 or age >60:
        return "Not Eligible"
    elif income <20000:
        return "Not Eligible"
    elif loan > 0.4 * income:
        return "Not Eligible"
    else:
        return "Eligible"
    
test_cases = [
    (25,300000,8000),
    (18,300000,5000),
    (30,15000,2000),
    (45,50000,25000),
    (21,20000,8000)
]

for tc in test_cases:
    print(tc, "->", check_eligibility(*tc))