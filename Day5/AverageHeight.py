# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇


total_height = 0
for height in student_heights:
  total_height += height
print(total_height)

numberofStudents = 0
for student in student_heights:
  numberofStudents += 1
print(numberofStudents)



# total_height = sum(student_heights)
numberOfStudents = len(student_heights)
average = round(total_height/numberOfStudents)
print(average)


