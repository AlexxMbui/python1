try:
    print(x)
except:
    print("NameError Occurred")

finally:
    print("success")

num1 = 20
num2 = 0
try:
    print(num1 / num2)
except:
    print("ZeroDivision Error Occurred")

# User-defined function
try:
    def multiply(x, y):
        return x * y
except:
    print("Exception occurred")
finally:print("success") # printed regardless of error


print(multiply(10,20))

