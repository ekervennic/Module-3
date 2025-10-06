# TODO: Create a string variable with a sentence

# TODO: Convert the string to uppercase

# TODO: Convert the string to lowercase

# TODO: Capitalize the first letter of each word

# TODO: Replace a word in the string

# TODO: Split the string into a list of words

# TODO: Join the list of words back into a string using a different separator

# TODO: Find the position of a specific word in the string

# TODO: Check if the string starts with a specific word

# TODO: Remove leading and trailing whitespace from a string

# Print the results of each operation
sentence = "Joyeux anniversaire"
print(sentence.replace("anniversaire", "birthday"))
print(sentence.split())
words_list = sentence.split()
print(words_list)
joined_sentence = "-".join(words_list)
print(joined_sentence)
print(sentence.find("anniversaire"))
starts_with_python = sentence.strip().startswith("Joyeux")
print(starts_with_python)
# TODO: Create variables for name, age, and height

# TODO: Use the .format() method to create a sentence with these variables

# TODO: Use f-strings to create the same sentence

# TODO: Use the % operator for string formatting

# TODO: Format a float number to display only two decimal places

# TODO: Create a table-like output using string formatting

# Print all formatted strings
name = "Elena"
age = 22 
height = 1.65
sentence = f"Je m'appelle {name}, j'ai {age}, je fais {height}"
print(sentence)
sentence_percent = "Je m'appelle %s, j'ai %d ans et je mesure %.2f m." % (name, age, height)
print(sentence_percent)
pi = 3.14159265
pi_formatted = "{:.2f}".format(pi)
print(pi_formatted)
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 22]
heights = [1.72, 1.85, 1.60]
for i in range(len(names)):
    print(names[i], ages[i], heights[i])
numbers = [1, 2, 3, 4, 5]
print("Boucle simple :")
for num in numbers:
    print(num)
for index, value in enumerate(numbers):
    print(f"Index {index} -> Valeur {value}")
person = {"name": "Alice", "age": 25, "city": "Paris"}
for key, value in person.items():
    print(f"{key} : {value}")
for i in range(1, 11):
    print(i)
squares = [x**2 for x in numbers]
print(squares)
print("\nTable de multiplication 5x5 :")
for i in range(1, 6):         
    for j in range(1, 6):      
        print(f"{i*j:3}", end=" ")  
    print()
# TODO: Use a while loop to print numbers from 1 to 10

# TODO: Create a guessing game using a while loop
# (generate a random number and let the user guess until correct)

# TODO: Use a while loop to calculate the factorial of a number

# TODO: Implement a simple calculator using a while loop
# (continue calculating until the user chooses to exit)
