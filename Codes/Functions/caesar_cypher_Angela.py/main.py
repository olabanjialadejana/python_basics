alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.


def caesar(text, shift, direction):
    final_word = ""
    for char in text:
        position = alphabet.index(char)
        if direction == "encode":
            new_position = position + shift
            final_word += alphabet[new_position]
        elif direction == "decode":
            new_position = position - shift
            final_word += alphabet[new_position]
    print(f'The new word is {final_word}')


caesar(text, shift, direction)
# TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
