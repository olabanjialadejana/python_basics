# You are going to write a program that tests the compatibility between two people.

# To work out the love score between two people:

# Take both people's names and check for the number of times the letters in the word TRUE occurs.

# Then check for the number of times the letters in the word LOVE occurs.

# Then combine these numbers to make a 2 digit number.

# For Love Scores less than 10 or greater than 90, the message should be:

# "Your score is **x**, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:

# "Your score is **y**, you are alright together."
# Otherwise, the message will just be their score. e.g.:

# "Your score is **z**."


# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
name1_low = name1.lower()
name2_low = name2.lower()

t = name1_low.count("t") + name2_low.count("t")
r = name1_low.count("r") + name2_low.count("r")
u = name1_low.count("u") + name2_low.count("u")
e = name1_low.count("e") + name2_low.count("e")

l = name1_low.count("l") + name2_low.count("l")
o = name1_low.count("o") + name2_low.count("o")
v = name1_low.count("v") + name2_low.count("v")
e = name1_low.count("e") + name2_low.count("e")

true = t + r + u + e
love = l + o + v + e

true_str = str(true)
love_str = str(love)
true_love_concat = true_str + love_str
true_love_num = int(true_love_concat)

if true_love_num < 10 or true_love_num > 90:
    print(
        f"Your score is {true_love_num}, you go together like coke and mentos.")
elif true_love_num >= 40 and true_love_num <= 50:
    print(f"Your score is {true_love_num}, you are alright together.")
else:
    print(f"Your score is {true_love_num}.")
