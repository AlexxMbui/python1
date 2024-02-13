class Person:
    def __init__(self,firstname,age,gender):
        self.firstname=firstname
        self.age=age
        self.gender=gender
    def details(self):
        print(self.firstname,"is studying")

teacher = Person("Jack",27,"male")
accountant = Person("Mary",30,"female")
doctor = Person("John",45,"male")



print(accountant.firstname,accountant.age,accountant.gender)

print(teacher.firstname,teacher.age,teacher.gender)


