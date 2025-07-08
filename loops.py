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

month = 7
year = 2025
days_in_month = 31

start_weekday = 1
special_days = [1, 15, 20]

print("Mo Tu We Th Fr Sa Su")

current_day = 1
week = []

i = 0
while i < start_weekday:
    week.append("  ")
    i += 1
while current_day <= days_in_month:
    if current_day in special_days:
        day_str = f"*{current_day:>2}"
    else:
        day_str = f" {current_day:>2}"

    week.append(day_str)


    if len(week) == 7:
        print(" ".join(week))
        week = []

    current_day += 1


if len(week) > 0:
    while len(week) < 7:
        week.append("  ")
    print(" ".join(week))
    