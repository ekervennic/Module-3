# TODO: Create a list of numbers

# TODO: Use a for loop to print each number in the list

# TODO: Use a for loop with enumerate() to print both index and value

# TODO: Create a dictionary and use a for loop to print all keys and values

# TODO: Use a for loop with range() to print numbers from 1 to 10

# TODO: Use list comprehension to create a new list of squares of numbers

# TODO: Use a nested for loop to create a multiplication table (up to 5x5)


# numbers = list(range(1, 11)) 
# for index, value in enumerate(numbers):
#     print(index, value)

# Alice = {
#     "name" : "Alice",
#     "age" : 22,
#     "city" : "Paris",
# }
# for key, value in Alice.items ():
#     print(key, value)

# for i in range(1, 6):       
#     for j in range(1, 6):     
#         print(i * j, end="\t") 
#     print()

# TODO: Use a while loop to print numbers from 1 to 10

# TODO: Create a guessing game using a while loop
# (generate a random number and let the user guess until correct)

# TODO: Use a while loop to calculate the factorial of a number

# TODO: Implement a simple calculator using a while loop
# (continue calculating until the user chooses to exit)

# i = 1
# while i <= 10:
#     print(i)
# \
# import random
# nombre_secret = random.randint(1, 10)
# devine = 0
# while devine != nombre_secret:
#     devine = int(input("Devinez le nombre entre 1 et 10 : "))  # demande la saisie
#     if devine < nombre_secret:
#         print("Trop petit !")
#     elif devine > nombre_secret:
#         print("Trop grand !")
#     else:
#         print("Bravo")

for i in range (1, 6): 
    for j in range (1, 11): 
        print(i*j)