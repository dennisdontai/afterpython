
firstnumber = float(input("Enter First Number:"))
secondnumber = float(input("Enter Second Number:"))
myoperator = str(input("Enter operator(+,-,/,*)"))

if myoperator=="+":
    print(firstnumber+secondnumber)
elif myoperator == "-":
    print(firstnumber -secondnumber)
elif myoperator == "*":
    print(firstnumber * secondnumber)
elif myoperator == "/":
    print(firstnumber / secondnumber)
else:
    print("invalid")

