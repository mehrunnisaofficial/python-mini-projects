"""
Ask for a sentence.
Print:
Original sentence
Total characters
Characters without spaces
"""


sentence = input("Hello user, can you please entr a sentence? ")

remove_space = sentence.replace(" ", "")

print(f"Total Chracter with spaces is : {len(sentence)},\nand the sentence is: \"{sentence}\"")
print(f"Total Chracter without spaces is : {len(remove_space)},\nand the sentence is: \"{remove_space}\"")
