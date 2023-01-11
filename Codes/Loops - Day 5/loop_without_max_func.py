# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
# step 1: We initialize a variable for the max_value and set it to the first element of the list.
max_score = student_scores[0]

# step 2: We go through all remaining elements in the list of numbers. You can use any type of loop you like.

for score in student_scores[1:len(student_scores)]:

    # step 3: Inside of the loop, we check for every element in the list, whether or not it is bigger than the value we stored in max_value.
    # If we found a value that is larger than the value that we stored in max_value, this means we found a value that is better suited to be our maximum.

    if max_score < score:

        # step 4: We overwrite our current candidate for the maximum with our newly found larger number
        max_score = score
print(f"The highest score in the class is: {max_score}")
