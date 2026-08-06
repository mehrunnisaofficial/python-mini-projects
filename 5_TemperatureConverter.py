"""
Question 5 - Temperature Converter

Formula:
F = (C × 9 / 5) + 32

Input:
Celsius

Output:
Temperature in Fahrenheit (rounded to 2 decimal places)
"""

# Get temperature in Celsius
celsius = float(input("Enter the temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32

# Method 1: Using round()
print(f"The temperature is {round(fahrenheit, 2)}°F.")

# or you can make a variable and than do thsi seprately
# roundoff = round(farenhite, 2)
# print(f"The temperature is {roundoff}°F.")  # generally I prefer this one

# Method 2: Using format specifier (Recommended)
print(f"The temperature is {fahrenheit:.2f}°F.")