from os import system

system('cls')
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_sum =0
for student in student_heights:
    total_sum +=  student

num = 0
for students in student_heights :
    num += 1

# calculating the average 
avg = total_sum/num

print(int(avg))


