# fruits = ["Apple", "Banana", "Cherry"]
# for i in fruits:
#     if i == "Banana":
#         continue
#     print(i)

# for z in range(6):
#     print(z)

# for a in "banana":
#     print(a)

# for x in range(6):
#     print(x)
# else:
#     print("Already Finished")

# kolade = ["risk","mivagirls","kolade"]
# mrprime = ["one","blue","stone"]
# for x in kolade:
#     for y in mrprime:
#         print(y,x)

# i = 0
# while i < 5:
#     print(i)  
#     i += 1


# count = 0
# while count < 5:
#     print(count)
#     count += 1

# for i in range(3):
#     for j in range(2):
#         print(f"i={i}, j={j}")

# for i in range(5):
#     if i == 2:
#         continue
#     print(i)

# month = 7
# year = 2025
# days_in_month = 31

# start_weekday = 1
# special_days = [1, 15, 20]

# print("Mo Tu We Th Fr Sa Su")

# current_day = 1
# week = []

# i = 0
# while i < start_weekday:
#     week.append("  ")
#     i += 1
# while current_day <= days_in_month:
#     if current_day in special_days:
#         day_str = f"*{current_day:>2}"
#     else:
#         day_str = f" {current_day:>2}"

#     week.append(day_str)


#     if len(week) == 7:
#         print(" ".join(week))
#         week = []

#     current_day += 1


# if len(week) > 0:
#     while len(week) < 7:
#         week.append("  ")
#     print(" ".join(week))
#     877



# month_names = [
#     "January", "February", "March", "April", "May", "June",
#     "July", "August", "September", "October", "November", "December"
# ]

# month_days = [31, 28, 31, 30, 31, 30,
#               31, 31, 30, 31, 30, 31]


# day_labels = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]


# year = 2025


# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     month_days[1] = 29


# def get_start_weekday(y, m):
#     if m < 3:
#         m += 12
#         y -= 1
#     k = y % 100
#     j = y // 100
#     weekday = (1 + ((13 * (m + 1)) // 5) + k + (k // 4) + (j // 4) + 5 * j) % 7
#     return (weekday + 6) % 7  


# for i in range(12):
#     name = month_names[i]
#     days = month_days[i]
#     start_day = get_start_weekday(year, i + 1)

#     print(f"\n{name} {year}")
#     print(" ".join(day_labels))

#     week = ["  "] * start_day
#     day = 1

#     while day <= days:
#         day_str = f"{day:>2}"
#         week.append(day_str) 

#         if len(week) == 7:
#             print(" ".join(week))
#             week = []

#         day += 1

#     if len(week) > 0:
#         while len(week) < 7:
#             week.append("  ")
#         print(" ".join(week))


# def my_function(fname):
    # print(fname + "Hello from a function")
# my_function("Kolade ")



# class MyClass:
#     x = 5
# p1 = MyClass()
# print(p1.x)


# class Car:
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color

#     def drive(self):
#         print(f"{self.color} {self.brand} is driving...")

# my_car = Car("Toyota", "White")
# my_car.drive()

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def greet(self):
#         print(f"Hello my name is {self.name} and i'm {self.age} years old")

# p1 = Person("Kolade", 18)
# p1.greet()

# class Store:
#     def __init__(self, sname, sdeal):
#         self.sname = sname
#         self.sdeal = sdeal

#     def welcomes(self):
#         print(f"Welcome to {self.sname}, here we sell {self.sdeal}")

# store = Store("Gabby Gadgets", "Iphones")
# store.welcomes()


# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year

#     def display_info(self):
#         print(f"{self.year} {self.brand} {self.model}")

# car = Car("Toyota", "Corolla", 2021)
# car.display_info()


# class Laptop:
#     def __init__(self, brand, ram, storage):
#         self.brand = brand
#         self.ram = ram
#         self.storage = storage

#     def specs(self):
#         print(f"Brand: {self.brand}, RAM: {self.ram}, Storage: {self.storage}")

# laptop = Laptop("HP", "8GB", "256GB")
# laptop.specs()

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def move(self):
#         print(f"{self.name} is moving")

# class Dog(Animal):
#     def bark(self):
#         print(f"{self.name} says woof!")

# d = Dog("Charlie")
# d.move()
# d.bark()


# class Animal:
#     def __init__(self, name):
#         self.name = name
#         print(f"Animal {self.name} created")

# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name)
#         self.breed = breed
#         print(f"Dog {self.name}, Breed: {self.breed} created")

# dog = Dog("Max", "German Shepherd")


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def speak(self):
#         print(f"My name is {self.name}, and i am {self.age} years old.")

# class Student(Person):
#     def __init__(self, name, age, student_id):
#         super().__init__(name, age)
#         self.student_id = student_id

#     def study(self):
#         print(f"Student {self.name} is studying...")

# s1 = Student("Teniola", 18, "MIV2025")
# s1.speak()
# s1.study()


# class Vehicle:
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color

#     def start(self):
#         print(f"The vehicle is starting.")

# class Car(Vehicle):
#     def __init__(self, brand, color, model):
#         super().__init__(brand, color)
#         self.model = model

#     def drive(self):
#         print(f"The {self.brand} {self.model} is driving...")

#     def start(self):
#         print(f"The car engine is starting...")

# my_car = Car("Toyota", "Red", "Corolla")
# my_car.start()
# my_car.drive()


# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def work(self):
#         print(f"{self.name} is working...")

# class Manager(Employee):
#     def __init__(self, name, salary, department):
#         super().__init__(name, salary)
#         self.department = department

#     def manage(self):
#         print(f"{self.name} is managing the {self.department} department.")

# my_manager = Manager("Kolade", 2000000, "Finance")
# my_manager.work()
# my_manager.manage()

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def make_sound(self):
#         print(f"{self.name} makes a sound..")

# class Dog(Animal):
#     def make_sound(self):
#         print(f"{self.name} says Woof!")
# class Cat(Animal):
#     def make_sound(self):
#         print(f"{self.name} says Meow!")

# dog1 = Dog("Buddy")
# cat1 = Cat("Whiskers")

# dog1.make_sound()
# cat1.make_sound()



# class Appliance:
#     def __init__(self, brand):
#         self.brand = brand

#     def power_on(self):
#         print(f"The {self.brand} appliance is now on.")

# class WashingMachine(Appliance):
#     def power_on(self):
#         print(f"{self.brand} washing machine is now washing clothes.")
# class Refrigerator(Appliance):
#     def power_on(self):
#         print(f"{self.brand} refridgerator is now cooling.")

# w1 = WashingMachine("Thermocool")
# r1 = Refrigerator("Thermocool")

# w1.power_on()
# r1.power_on()


# class Device:
#     def __init__(self, brand):
#         self.brand = brand

#     def turn_on(self):
#         print(f"The {self.brand} is turning on.")

# class Phone(Device):
#     def turn_on(self):
#         print(f"{self.brand} is starting up...")
# class Laptop(Device):
#     def turn_on(self):
#         print(f"{self.brand} laptop is booting...")


# p1 = Phone("Iphone")
# l1 = Laptop("Hp")

# p1.turn_on()
# l1.turn_on()

# class Animal:
#     def move(self):
#         print(f"Animal is moving")

# class Fish(Animal):
#     def swim(self):
#         print(f"Fish is swimming")

# f = Fish()
# f.move()
# f.swim()

# class GrandParent:
#     def say_hello(self):
#         print("Hello from Grandpa!")

# class Parent(GrandParent):
#     pass

# class Child(Parent):
#     pass


# baby = Child()
# baby.say_hello()



class User:
    def __init__(self, username):
        self.username = username

    def login(self):
        print(f"{self.username} has logged in.")

class Admin(User):
    def delete_user(self):
        print(f"{self.username} deleted a user")

admin1 = Admin("Gabriel")
admin1.login()
admin1.delete_user()

//