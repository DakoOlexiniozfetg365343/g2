class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Student(Person):
    mark = 1
    def __init__(self,name):
        super().__init__(name, 15)


good_student1 = Student("Sasha")
good_student2 = Student("Slavik")

print(good_student1.mark)
