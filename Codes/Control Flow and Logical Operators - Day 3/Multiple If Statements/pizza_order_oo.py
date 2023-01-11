# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if size == "S":
    final_bill = 15
    if add_pepperoni == "N" and extra_cheese == "N":
        print(f"Your final bill is: ${final_bill}.")
    elif add_pepperoni == "Y" and extra_cheese == "Y":
        final_bill += 3
        print(f"Your final bill is: ${final_bill}.")
    elif add_pepperoni == "N" and extra_cheese == "Y":
        final_bill += 1
        print(f"Your final bill is: ${final_bill}.")
    elif add_pepperoni == "Y" and extra_cheese == "N":
        final_bill += 2
        print(f"Your final bill is: ${final_bill}.")

elif size == "M":
    final_bill = 20
    if add_pepperoni == "N" and extra_cheese == "N":
        print(f"Your final bill is: ${final_bill}.")
    elif add_pepperoni == "Y" and extra_cheese == "Y":
        final_bill += 4
        print(f"Your final bill is: ${final_bill}.")
    elif add_pepperoni == "N" and extra_cheese == "Y":
        final_bill += 1
        print(f"Your final bill is: ${final_bill}.")
    elif add_pepperoni == "Y" and extra_cheese == "N":
        final_bill += 3
        print(f"Your final bill is: ${final_bill}.")

elif size == "L":
    final_bill = 25
    if add_pepperoni == "N" and extra_cheese == "N":
        print(f"Your final bill is: ${final_bill}.")
    elif add_pepperoni == "Y" and extra_cheese == "Y":
        final_bill += 4
        print(f"Your final bill is: ${final_bill}.")
    elif add_pepperoni == "N" and extra_cheese == "Y":
        final_bill += 1
        print(f"Your final bill is: ${final_bill}.")
    elif add_pepperoni == "Y" and extra_cheese == "N":
        final_bill += 3
        print(f"Your final bill is: ${final_bill}.")
else:
    print("follow the prompt")
