# a simple calculator
num1 = float(input("Enter Value 1:"))
num2 = float(input("Enter Value 2:"))
operator = input("Enter operator sign")
if operator == "+":
    result = num1+num2
elif operator == "-":
    result = num1 -num2
elif operator == "*":
    result = num1*num2

elif operator == "/":
    result = num1/num2
else:result == "invalid"


print("the result of the calculation is",result)