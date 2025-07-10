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