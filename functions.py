# In-built functions
number = max(45,88,76,90,75)
print(number)

num = min(34,67,34,65,99)
print(num)

x = pow(2,3)
print(x)

# user-defined functions
def name():
    print("Alex")
name() # calling a function


def student():
    name = "vincent"
    age = 18
    course = "MIT"
    print(name,age,course)
student()

def students(name,age,course):
    print(name,age,course)

students("Brian",18,"MIT")
students("Collins",19,"Cybersecurity")
students("Curtis",17,"Cybersecurity")

# User defined function called employees displaying 5 employee details
# parameters are fullname,age,gender, position,salary

def employees(fullname,age,gender,position,salary):
    print(fullname,age,gender,position,salary)

employees("Allan Kuria",26,"Male","chief manager",300000)
employees("Moses Abdi",29,"Male","administrative manager",250000)
employees("Alice Kutu",33,"Female","operations manager",200000)
employees("Bruce Monyancha",24,"Male","secretary",80000)
employees("Bradley Kiptoo",22,"Male","receptionist",60000)



