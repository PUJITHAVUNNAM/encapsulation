class Student:
    def __init__(self, marks):
        self.__marks = marks

    def update_marks(self, marks):
        if marks >= 0 and marks <= 100:
            self.__marks = marks
            print("Marks updated successfully")
        else:
            print("Invalid marks")

    def display(self):
        print("Marks:", self.__marks)


s = Student(80)

s.display()

s.__marks = 150
s.display()
s.update_marks(90)
s.display()
s.update_marks(150)
s.display()