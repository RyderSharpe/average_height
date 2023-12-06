# Input a Python list of student heights

# takes input from the user, assuming the heights are entered as space-separated values. It splits the input into a list of strings.
student_heights = input().split()
# initiates a for loop that iterates through the indices of the student_heights list.
for n in range(0, len(student_heights)):
    # Inside the loop, each element in the list is converted to an integer using the int() function.
    student_heights[n] = int(student_heights[n])

# 🚨 Don't change the code above 👆

# Write your code below this row 👇
# Sum of heights. iterate through the list of heights and add each height to a variable that keeps track of the total sum.

num_students = 0
total_height = 0
# height_sum is a variable that takes on the value of each element in the list student_heights during each iteration.
for height_sum in student_heights:
    total_height += height_sum
    num_students += 1

print(f"total height = {total_height}")
print(f"number of students = {num_students}")
average_height = round(total_height / num_students) # round or int
print(f"average height = {average_height}")
