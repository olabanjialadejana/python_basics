# THis code pick out who will pay the bills from a given number of friends
# it also attempts not to utilize  choice from the random module. I tried to do things manually just go grasp it further

import random

# name = input("List the names of all friends seperated by a comma\n")
name = "Kemi, Femi, Tunji, Bode, Toyin"

# split the names of the friends and convert it to a list
name_split = name.split(",")

choice = random.randint(0, len(name_split)-1)
payer = name_split[choice]
print(f"{payer} will pay the bills")
