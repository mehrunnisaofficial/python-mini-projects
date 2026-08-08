# Create dictionary
# Ask
# Name
# City
# Age
# Store everything.
# Print
# Name : John
# City : Delhi
# Age : 20

def main():
    times = get_times()

    students = []

    for _ in range(times):
        student = {
            "student_name": get_name(),
            "student_city": get_city(),
            "student_age": get_age()
        }

        students.append(student)

    for student in students:
        print()
        print(f"Name = {student['student_name']}")
        print(f"City = {student['student_city']}")
        print(f"Age = {student['student_age']} years old")


# ASKING NAME FROM THE USER

def get_name():
    while True:
        name = input("Enter your name: ").strip().title()

        edit_name = name.split()

        if edit_name and all(word.isalpha() for word in edit_name):
            return " ".join(edit_name)
        else:
            print("Please enter your name")

# ASKING CITY FROM USER

def get_city():
    while True:
        city = input("Enter your city name: ").strip().title()

        edit_city = city.split()

        if edit_city and all(word.isalpha() for word in edit_city):
            return " ".join(edit_city)
        else:
            print("Please enter your city name")

# ASKING AGE FROM THE USER

def get_age():
    while True:
        try:
            age = int(input("Enter your age: "))

            if age > 0:
                return age

            print("ENTER POSITIVE NUMBER")

        except ValueError:
            print("Please enter your age!!!")

# ASKING HOW MANY STUDENTS USER WANNA STORE?

def get_times():
    while True:
        try:
            times = int(input("Enter how many students data you wanna store: "))

            if times > 0:
                return times

            print("Please enter positive number")

        except ValueError:
            print("It's not a number")


main()




"""
### What I did with this code

Brooo, I kinda edited this code a LOT, a LOT means a LOTTTT 😭. 
I started with a simple dictionary that stores a student's name, city, and age, 
but then I kept adding stuff and making it more useful. (which Ik wasn't asked)

Now it can store multiple students, validate the inputs, 
handle invalid ages, clean up names and cities, 
and deal with extra spaces too. 💀

I know I made the original problem more advanced than it needed to be, 
but I actually tried to keep the logic easy and readable 
instead of making it unnecessarily complicated.

Basically, I started with a tiny dictionary and 
somehow turned it into a mini student-data program. 😭

"""