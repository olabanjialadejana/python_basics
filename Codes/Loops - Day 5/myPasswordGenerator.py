# Program to generate passwords automatically

import string
import random

# Generate all the available letters in english language
get_letters = string.ascii_letters

# Convert the obtained letters to a string of individual characters
letters = [* get_letters]


# Generate all available numbers (0 - 9)
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Generate all spacial characters for the password
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Receive number of letters, numbers, and symbols to be used for the password
# combination from the user.
nr_letters = int(
    input("How many letters do you want to use in the password?\n"))
nr_numbers = int(
    input("How many numbers do you want to use in the password?\n"))
nr_symbols = int(
    input("How many symbols do you want to use in the password?\n"))


# Generate the random letters based on user specification
random_letters = []
for letter in range(0, nr_letters):
    choice_letter = random.choice(letters)
    random_letters += choice_letter


# Generate the random numbers based on user specification
random_numbers = []
for number in range(0, nr_numbers):
    choice_number = random.choice(numbers)
    random_numbers += choice_number


# Generate the random symbols based on user specification
random_symbols = []
for symbol in range(0, nr_symbols):
    choice_symbol = random.choice(symbols)
    random_symbols += choice_symbol


# Convert the generated random numbers list to a single string
chosen_numbers = ''
for x in random_numbers:
    chosen_numbers += '' + x


# Convert the generated random letters list to a single string
chosen_letters = ''
for x in random_letters:
    chosen_letters += '' + x


# Convert the generated random symbols list to a single string
chosen_symbols = ''
for x in random_symbols:
    chosen_symbols += '' + x


# Print out the final password
final_password = chosen_numbers+chosen_letters+chosen_symbols
print(f"The easy password is {final_password}")  # This is the easy result

# Here is an attempt to make the password stronger by randomizing the final password obtained

# Convert the final_password to list. This makes it easy to use the .shuffle method from the random module and generate a new final password list (final_password_list)
final_password_list = list(final_password)
random.shuffle(final_password_list)

# Since its now randomized, run a loop to pull out the randomized characters.
final_password_list_hard = ''
for y in final_password_list:
    final_password_list_hard += '' + y

# Print out the final stronger password!!!!!!
print(f"The hard password is {final_password_list_hard}")
