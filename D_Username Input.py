#Question: 1
"""
Ask the user for:
First name
Last name
Remove extra spaces.
Print:
Hello, John Doe!
Welcome to Python.

"""

#name = input("Hello user, Can you please enter your name here? ").title().strip() #another way to do the same thing

# name = input("Hello user, Can you please enter your name here? ")

# adjusting = name.strip().title()      

# print(f"Hello, {adjusting}!\nWelcome to Python.")

# better way
# if user enetr more than 3 words in his/her name
# than still the code will run without any bugs :)

full_name = input(
    "Hello user, can you please enter your name? "
).strip().title()

parts = full_name.split()

if len(parts) == 1:
    print(f"Hello {parts[0]}!\nWelcome to Python.")
else:
    print(f"Hello, {parts[0]} {parts[-1]}!\nWelcome to Python.")



