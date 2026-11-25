class Student:
    def __init__(self, age):
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value > 0:
            self.__age = value
        else:
        print("Invalid age")

s = Student(21)

print(s.age)

s.age = 25
print(s.age)

s.age = -5
print(s.age)