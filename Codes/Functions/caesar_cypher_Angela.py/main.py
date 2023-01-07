import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)


# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.


def caesar(text, shift, direction):
    final_word = ""
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            if direction == "encode":
                new_position = position + shift
                if new_position > 25:
                    new_position = new_position % 25
                final_word += alphabet[new_position]
            elif direction == "decode":
                new_position = position - shift
                final_word += alphabet[new_position]
        else:
            final_word += char
    print(f'The new word is {final_word}')


answer = True
while answer:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    user_continue = input(
        "Do you want to continue? if yes, type (y), if no, type (n)\n").lower()
    if user_continue == "n":
        answer = False
        print("Thanks for using Caesar's Cypher. Goodbye!!!")
