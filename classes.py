'''Parent class called Person'''
class Person:
    def __init__(self,get_name:str,get_age:int):
        self.name=get_name
        self.age=get_age

    def speak(self):
        print("Hello")

    def walk(self):
        print("walking away")

person1=Person("Tom",27)
print(person1.name)


'''subclass called Student'''
class Student:
    def __init_subclass__(self,get_courses:list[str],get_name:str,get_age:int):
        self.courses=get_courses
        self.name=get_name
        self.age=get_age

    def speak(self):
        print("I'm so tired!")

stud1=Student(["STAT 112", "MATH 121", "DCIT 104"],"Nana",23)
print(stud1.speak())
print(stud1.courses)
print(stud1.name)
print(stud1.age)


