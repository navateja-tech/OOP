from abc import ABC , abstractmethod

class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name : {self.name} , Age : {self.age}"


class Student(Person):
    def __init__(self, name , age, roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.__grades = []

    def add_grade(self, grade):
        if 0<= grade <=100:
            self.__grades.append(grade)
        else:
            raise ValueError("Grades should be in the range of 0 to 100")

    def average_grade(self):
        if self.__grades:
            return sum(self.__grades)/len(self.__grades)
        else:
            return 0 

    def __eq__(self, other ):
        if isinstance(other, Student):
            return True if self.roll_no == other.roll_no else False
        else:
            raise ValueError("cant compare two different objects")

    def __str__(self):
        return f"{super().__str__()}, Roll no : {self.roll_no}"
    



class Teacher(Person):
    def __init__(self, name , age, subject):
            super().__init__(name, age)
            self.subject = subject
           

    def __str__(self):
        return f"{super().__str__()} , Subject : {self.subject}"