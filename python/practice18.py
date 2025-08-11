marks = int(input("Enter the marks of students: "))

if 100 >= marks >= 90:
    grade = 'Ex'
elif 89 >= marks >= 80:
    grade = 'A'
elif 79 >= marks >= 70:
    grade = 'B'
elif 69 >= marks >= 60:
    grade = 'C'
elif 59 >= marks >= 50:
    grade = 'D'
elif 49 >= marks >= 40:
    grade = 'E'
else:
    grade = 'F'

print("Marks:", marks)
print("Grade:", grade)
