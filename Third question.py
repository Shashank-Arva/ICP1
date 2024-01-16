# Use the if statement conditions to write a program to print the letter grade based on an input class score.

# Receive the class score input from the user
class_score = float(input("Provide the score for the class: "))

# Decide the letter grade according to the grading criteria
if 90 <= class_score <= 100:
    grade = 'A'
elif 80 <= class_score < 90:
    grade = 'B'
elif 70 <= class_score < 80:
    grade = 'C'
elif 60 <= class_score < 70:
    grade = 'D'
elif 0 <= class_score < 60:
    grade = 'F'
else:
    grade = 'Not a valid score'

# Print the assigned letter grade
print(f"Letter Grade: {grade}")
