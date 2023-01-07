import string
import random

alphabets = string.ascii_letters
letters = list(alphabets)

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

user_letters = int(input("How many letters do you want?"))
user_numbers = int(input("How many numbers do you want?"))
user_symbols = int(input("How many symbols do you want?"))

choice_letters = ''
for char in range(user_letters):
    choice_letters += random.choice(letters)


choice_numbers = ''
for char in range(user_numbers):
    choice_numbers += random.choice(numbers)


choice_symbols = ''
for char in range(user_symbols):
    choice_symbols += random.choice(symbols)


easy_password = choice_letters+choice_numbers+choice_symbols
print(easy_password)

easy_password_list = list(easy_password)
random.shuffle(easy_password_list)
hard_password = ''
for x in easy_password_list:
    hard_password += x
print(hard_password)
