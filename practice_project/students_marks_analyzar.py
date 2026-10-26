# Write a Python program that stores student information and analyzes their marks.

# Your program must:
# 1. Input validation: Keep asking the user to enter the number of students until they enter a positive number.
# 2. Loops: Use a for loop to collect each student's name and marks in three subjects.
# 3. Lists: Store the three subject marks in a list for each student.
# 4. Dictionaries: Store each student's name and marks in a dictionary.
# 5. Lists of dictionaries: Store all students' dictionaries in one list.
# 6. len(): Display the total number of students.
# 7. Iteration: Loop through the list to display each student's name and marks.
# 8. Nested loops: Calculate the total marks of each student by iterating through their marks list.
# 9. while loop: Keep asking for a student's name until the user enters "stop" when searching for a student.
# 10. Output: Display each student's total marks and average marks.



# def main():


#     analyzes_marks(marks);

# def validation(num):
#     if num<0:
#         print("negative numbers are not allowed")
#     else:
#         return num;




students=int(input("enter the number of sudents"))
name=input("enter your name")
subject=int(input("enter number of subject:"))
marks=int(input("enter youe marks"))

for i in range(subject):
    
