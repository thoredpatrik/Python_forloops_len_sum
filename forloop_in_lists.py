
#Using for-loops for the functions of len() and sum() in lists

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
    total_height += height

number_students = 0
for student in student_heights:
    number_students += 1

avarege_lenght = round(total_height/number_students)
print (avarege_lenght)