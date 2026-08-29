"""
Question 16 - Student Result System

Ask:
- Name
- Roll Number
- Marks in English
- Marks in Maths
- Marks in Science

Calculate:
- Total
- Percentage
- Grade

Store multiple students' data.
"""


def main():
    times = get_student_list()
    data = []

    for _ in range(times):
        name = get_name()
        roll_number = roll_no()
        obtained_marks = get_marks()

        total_marks = 300
        total_obtained = sum(obtained_marks.values())
        percentage = (total_obtained / total_marks) * 100
        grade = get_grade(percentage)

        student_data = {
            "Name": name,
            "Roll Number": roll_number,
            "Total Marks": total_marks,
            "Obtained Marks": total_obtained,
            "English": obtained_marks["English"],
            "Maths": obtained_marks["Maths"],
            "Science": obtained_marks["Science"],
            "Percentage": percentage,
            "Grade": grade
        }

        data.append(student_data)

    for student in data:
        print()
        print(f"Name: {student['Name']}")
        print(f"Roll Number: {student['Roll Number']}")
        print(f"Total Marks: {student['Total Marks']}")
        print(f"Obtained Marks: {student['Obtained Marks']}")
        print(f"English: {student['English']}")
        print(f"Maths: {student['Maths']}")
        print(f"Science: {student['Science']}")
        print(f"Percentage: {student['Percentage']:.2f}%")
        print(f"Grade: {student['Grade']}")
        


def get_student_list():
    while True:
        try:
            student_list = int(
                input("Enter How many student data you wanna store: ")
            )

            if student_list > 0:
                return student_list

            print("Please enter a positive number of students.")

        except ValueError:
            print("Please enter a number.")


def get_name():
    while True:
        name = input("Enter your name: ").strip().title()
        edit_name = name.split()

        if edit_name and all(word.isalpha() for word in edit_name):
            return " ".join(edit_name)

        print("Please enter a valid name using alphabets only.")


def roll_no():
    while True:
        try:
            roll_number = int(input("Enter your Roll Number: "))

            if roll_number > 0:
                return roll_number

            print("Please enter a positive Roll Number.")

        except ValueError:
            print("Please enter a number.")


def get_marks():
    subject_marks = {
        "English": get_subject_marks("English"),
        "Maths": get_subject_marks("Maths"),
        "Science": get_subject_marks("Science")
    }

    return subject_marks


def get_subject_marks(subject):
    while True:
        try:
            marks = int(input(f"Enter Marks of {subject}: "))

            if 0 <= marks <= 100:
                return marks

            print("Please enter marks between 0 and 100.")

        except ValueError:
            print("Please enter a number.")


def get_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


main()




#------

"""
Aghhh this code was kinda hectic
took an hour to complete
now don't judge please 
cause I am just a beginner too
like u all guys
and finally after lot's of efforts
I completed it
Still it have lot's of issue
but I will try to sort it out later
Now I am going to sleep
Ba-Bye

"""