import impl, funcs

impl.calc()


marks = int(input("Enter marks: "))

if funcs.pass_or_fail(marks):
    print("PASS")
else:
    print("FAIL")
