# Write a program to calculate area of a circle.

# formula = pi * r^2

while True:
    try:
        radius = float(input("Enter the radius of a circle: "))

        if radius < 0:
            print("Radius Can't be Negative")
        else:
            break
    except ValueError:
        print("Wrong Value Please try again")

units = { 1: "m", 2: "cm", 3: "km" }

print("Units options:")

for key, unit in units.items():
    print(f"{key}. {unit}")


while True:
    try:
        user_input = int(input("Choose a unit (give a number): "))

        if user_input in units:
            break
        else:
            print("Please choose a valid option.")

    except ValueError:
        print("Please enter a number.")

    

area = 3.14 * radius * radius
print(f"The area of a circle is {area} square {units[user_input]} ")

