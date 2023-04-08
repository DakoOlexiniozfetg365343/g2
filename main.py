class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Student(Person):
    mark = 1
    def __init__(self,name):
        super().__init__(name, 15)

class Teacher(Person):

    def __init__(self,name):
        super().__init__(name, 25)


    def give_mark(self, student):
        print("Teacher gave grade to", student.name)
        student.mark = 12




good_student1 = Student("Sasha")
good_student2 = Student("Slavik")
teacher = Teacher("Kiril")

teacher.give_mark(good_student1)
teacher.give_mark(good_student2)
print(good_student1.mark)

