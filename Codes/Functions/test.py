from random_word import RandomWords

# Generate a random word
my_random_word = RandomWords()
random_word = list(my_random_word.get_random_word())
print(random_word)

# Generate as many blanks as letters in the generated random word
blanks = []
for _ in random_word:
    blanks += '_'
print(blanks)

# Ask user to guess a letter


# Replace guessed letter with its position in the blank spaces generated
lives = len(random_word) + 1
attempts = 0
while attempts < lives:
    for position in range(len(random_word)):
        attempts += 1
        letter = random_word[position]
        guess = input("Please guess a letter \n").lower()
        if letter == guess:
            blanks[position] = letter
            print(blanks)
        else:
            print("Make another attempt")
print("You failed")
