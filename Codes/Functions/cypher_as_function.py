import string
import logo

print(logo.caesar_cypher)

# Generate a list of all ascii lowercase letters
letters = string.ascii_lowercase
# print(letters)
list_of_letters = list(letters)
# print(list_of_letters)

# Receive word to be encrpyted from user. Make sure to convert the message to a list
# received = list(input("Type your message: \n").lower())
# print(received)

# Get the shift number from user
# shift_number = int(input("Type the shift number\n"))


def cypher(received, shift_number):
    # Loop through the received word list and add the "specified shift number for encryption" to the index number. Append the result (i.e. indexes to position_number)
    position_number = []
    for char in received:
        test = list_of_letters.index(char) + shift_number
        position_number.append(test)
    print(position_number)

    # Loop through the position number list and add the extract the character at position number indexes to position letter
    position_letter = []
    for char in position_number:
        fig = list_of_letters[char]
        position_letter.append(fig)
    print(position_letter)

    # position letter will be a list. use the join function to turn it to string
    final = "".join(position_letter)
    return (f"Here is the encoded result: {final}")


received = list(input("Type your message: \n").lower())
shift_number = int(input("Type the shift number\n"))

cool = cypher(received, shift_number)
print(cool)
