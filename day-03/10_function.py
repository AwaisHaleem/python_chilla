# defining function
def print_codanics():
    print("Condanics")
    print("Condanics")
    print("Condanics")
    print("Condanics")


print_codanics()

# function with arguments


def print_text(text):
    print(text)
    print(text)
    print(text)


text = "I'm learning python with ammar"
print(print_text(text))


# defining a fucntion with conditionals
def school_age_calclator(age, school_age):
    if age == school_age:
        print("Congratulations! hammad can join the school")
    elif age > school_age:
        print("Hammad can join high school")
    elif age <= 2:
        print("Hammad is infant! take care of him")
    else:
        print("Hammad can't join the school")


def future_age(age):
    new_age = age + 20
    return new_age


future_age = future_age(30)
print(future_age)
