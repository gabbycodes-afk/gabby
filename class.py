class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def display_all(self):
        print(f"My name is {self.name} and i'm {self.age} years old and i'm in {self.grade}")

s1 = Student("Gabby", 16, "Grade 10")
s1.display()
s1.display_all()

class Animal:
    def make_sound(self):
        print("Animal makes a sound.")

class Mammals(Animal):
    def walk(self):
        print("Mammal walks")

class Dog(Mammals):
    def bark(self):
        print("Woof! Woof!")

dog = Dog()
dog.make_sound()
dog.walk()
dog.bark()