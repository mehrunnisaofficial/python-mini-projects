"""
Question 12 - Animal Repeater
Ask
Dog

Ask
How many times?

Output
Dog
Dog
Dog

Use for loop.
"""


def main():
    word = get_word()
    how_many_times = get_times()
    for _ in range(how_many_times):
        print(word)


def get_word():
    while True:
        word = input("Please enter a word: ").strip()

        if word.isalpha():
            return word
        else:
            print("Please enter letters only.")

def get_times():
    while True:
        try:
            num = int(input("Enter how many times you wanna print this word: "))

            if num > 0:
                return num

            print("ENTER POSITIVE NUMBER")

        except ValueError:
            print("It's not a number.")


main()
    



# code Explanation and My mistake
# def main():
#     word = asking_word()
#     how_many_times = call_times()
#
#     for _ in range(how_many_times):
#         print(word)
#
#
# def asking_word():
#     words = input("Please enter a word: ")
#
#     while True:
#         if words.isalpha():
#             call_times()
#             return words
#         else:
#             print("Try again")
#
#
# def call_times():
#     while True:
#         try:
#             num = int(input("Enter how many times you wanna print this word: "))
#         except:
#             print("It's not a number")
#         else:
#             return num
#
#
# main()


# HOW PYTHON EXECUTES THIS PROGRAM
#
# Step 1:
# The program starts from main().
#
# Step 2:
# Python executes:
#
#     word = asking_word()
#
# As soon as this line is reached, Python pauses main() and jumps into
# the asking_word() function. Nothing after this line in main() executes
# until asking_word() returns.
#
# Step 3:
# The user is asked to enter a word.
#
# Suppose the user enters:
#
#     123
#
# Now:
#
#     words = "123"
#
# Step 4:
# Python reaches:
#
#     while True:
#
# Since True is always True, Python enters the loop.
#
# Step 5:
# Python checks:
#
#     words.isalpha()
#
# Since "123" is not alphabetic,
#
#     words.isalpha() == False
#
# Step 6:
# Python executes:
#
#     print("Try again")
#
# At first I thought that after printing "Try again",
# Python would go back to main() and continue executing:
#
#     how_many_times = call_times()
#
# But that is NOT what happens.
#
# Python is STILL inside asking_word().
#
# There is no break.
# There is no return.
#
# So Python reaches the end of the while loop and automatically
# goes back to the top because of:
#
#     while True
#
# Step 7:
# Python again checks:
#
#     words.isalpha()
#
# But the important thing is:
#
#     words is STILL "123"
#
# because I only asked for input once.
#
# I never asked the user for another word.
#
# So Python again checks:
#
#     "123".isalpha()
#
# It is still False.
#
# It prints:
#
#     Try again
#
# Then it loops again.
#
# Again.
# Again.
# Again.
#
# Forever.
#
#
# WHY IT BECOMES AN INFINITE LOOP
#
# The problem is NOT while True.
#
# The real problem is that the value of "words" never changes.
#
# I asked for input only once:
#
#     words = input(...)
#
# Since this line is outside the while loop,
# Python keeps checking the SAME invalid input forever.
#
#
# ANOTHER MISTAKE
#
# Inside asking_word() I called:
#
#     call_times()
#
# This is unnecessary because main() already calls call_times().
#
# So the program asks for the number twice,
# even though only one value is actually needed.
#
#
# BIGGEST LESSON
#
# A function does NOT go back to main() until it reaches a return
# or the function ends.
#
# A while True loop keeps looping until it reaches a break or a return.
#
# If the data inside the loop never changes,
# the loop will continue forever.
# after writing wrong code I felt stupid
