"""
Question 9 - Password Checker
Correct password
python123

Keep asking until the user enters it correctly.
After success
Access Granted!

"""


# with time limit
for _ in range(5):
    password = input("Please enter your password sir: ").strip().lower()

    if password == "python123":
        print("Access Granted!")
        break
    else:
        print("Wrong password. Please try again.")



# without time limit
# while True:
#     password = input("Please enter your password sir: ").strip().lower()
#     if (password == "python123"):
#         print("Access Granted!")
#         break
#     else:
#         print("Wrong password. Please try again.")