"""
Question 3 - Username Generator

Input:
John Michael Doe

Output:
john_michael_doe

Requirements:
- Convert to lowercase
- Remove extra spaces
"""

# Get the user's full name
name = input("Hello user, can you please enter your name? ").lower()

# Split the name into words and join them with underscores
username = "_".join(name.split())

# Display the generated username
print(f"Your username is:\n{username}")





"""
Other ways to do the same code
but these methods will lack some features

# Method 1 (Not Recommended)

# Problem:
# replace() changes every space into "_".
# If the user enters multiple spaces,
# multiple underscores will also appear.

# name = input("Hello user, can you please enter your name? ").strip().lower()
# username = name.replace(" ", "_")
# print(f"Your username is:\n{username}")



# Method 2 (Works, But Limited)

# Problem:
# This only works if the user has a fixed
# number of names (e.g., first, middle, last).
# It can raise an IndexError if fewer names
# are entered.

# name = input("Hello user, can you please enter your name? ").lower()
# username = name.split()
# print(f"Your username is:\n{username[0]}_{username[1]}_{username[-1]}")


"""