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
# sentence = "Joyeux anniversaire"
# print(sentence.replace("anniversaire", "birthday"))
# print(sentence.split())
# words_list = sentence.split()
# print(words_list)
# joined_sentence = "-".join(words_list)
# print(joined_sentence)
# print(sentence.find("anniversaire"))
# starts_with_python = sentence.strip().startswith("Joyeux")
# print(starts_with_python)
# TODO: Create variables for name, age, and height

# TODO: Use the .format() method to create a sentence with these variables

# TODO: Use f-strings to create the same sentence

# TODO: Use the % operator for string formatting

# TODO: Format a float number to display only two decimal places

# TODO: Create a table-like output using string formatting

# Print all formatted strings
# name = "Elena"
# age = 22 
# height = 1.65
# sentence = f"Je m'appelle {name}, j'ai {age}, je fais {height}"
# print(sentence)
# sentence_percent = "Je m'appelle %s, j'ai %d ans et je mesure %.2f m." % (name, age, height)
# print(sentence_percent)
# pi = 3.14159265
# pi_formatted = "{:.2f}".format(pi)
# print(pi_formatted)
# names = ["Alice", "Bob", "Charlie"]
# ages = [25, 30, 22]
# heights = [1.72, 1.85, 1.60]
# for i in range(len(names)):
#     print(names[i], ages[i], heights[i])
# numbers = [1, 2, 3, 4, 5]
# print("Boucle simple :")
# for num in numbers:
#     print(num)
# for index, value in enumerate(numbers):
#     print(f"Index {index} -> Valeur {value}")
# person = {"name": "Alice", "age": 25, "city": "Paris"}
# for key, value in person.items():
#     print(f"{key} : {value}")
# for i in range(1, 11):
#     print(i)
# squares = [x**2 for x in numbers]
# # print(squares)
# # print("\nTable de multiplication 5x5 :")
# # for i in range(1, 6):         
# #     for j in range(1, 6):      
# #         print(f"{i*j:3}", end=" ")  
# #     print()
# # TODO: Create a list of numbers

# # TODO: Use a for loop to print each number in the list
# numbers = [2,3,4,5,6,7]
# print(numbers)

# for index, value in enumerate(numbers):
#     print("Index :", index, "→ Valeur :", value)
# # TODO: Use a for loop with enumerate() to print both index and value
# person = {"nom": "Alice", "âge": 25, "ville": "Paris"}

# for key, value in person.items():
#     print(key, ":", value)
# # TODO: Create a dictionary and use a for loop to print all keys and values

# # TODO: Use a for loop with range() to print numbers from 1 to 10
# for i in range(1, 11):
#     print(i)
# # TODO: Use list comprehension to create a new list of squares of numbers
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(squares)
# print(squares)
# # TODO: Use a nested for loop to create a multiplication table (up to 5x5)
# for i in range(1, 6):
#     for j in range(1, 6):
#         print(f"{i*j:3}", end=" ")
#     print()
# # TODO: Use a while loop to print numbers from 1 to 10
# i = 1
# while i <= 10:
#     print(i)
#     i += 1
# TODO: Create a guessing game using a while loop
# (generate a random number and let the user guess until correct)

# TODO: Use a while loop to calculate the factorial of a number

# TODO: Implement a simple calculator using a while loop
# (continue calculating until the user chooses to exit)
# i = 1
# while i <= 10:
#     print(i)
#     i += 1
# import random
# secret = random.randint(1, 10)
# guess = 0

# while guess != secret:
#     guess = int(input("Devine un nombre entre 1 et 10 : "))
#     if guess < secret:
#         print("Trop petit !")
#     elif guess > secret:
#         print("Trop grand !")
#     else:
#         print("Bravo, tu as trouvé ! 🎉")

# n = int(input("Entre un nombre : "))
# fact = 1
# i = 1

# while i <= n:
#     fact *= i
#     i += 1

# print(f"La factorielle de {n} est {fact}")
# while True:
#     operation = input("Entrez une opération (ex: 2 + 3) ou 'exit' pour quitter : ")

#     if operation.lower() == "exit":
#         print("Au revoir 👋")
#         break

#     try:
#         result = eval(operation)  # calcule l'expression saisie
#         print("Résultat =", result)
#     except:
#         print("Erreur de calcul ❌")
# TODO: Create a function that counts the occurrence of each vowel in a string


# TODO: Implement a simple Caesar cipher (shift each letter by a fixed amount)

# TODO: Create a function that generates the NATO phonetic alphabet representation of a word

# TODO: Implement a function that checks if a string is a palindrome

# Test each function with sample inputs and print the results

city = ["Paris", "New York", "Lyon"]
for i in city:
    print(i)
