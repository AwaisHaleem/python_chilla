# while and for loops

# while loops
x = 0
while x < 5:
    print(x)
    x += 1

for x in range(5, 11):
    print(x)


days = ["mon", "tue", "wed", "thur", "friday", "sat", "sunday"]

for day in days:
    # if day == "thur":
    #     break
    if (day == "thur"):
        continue
    print(day)
