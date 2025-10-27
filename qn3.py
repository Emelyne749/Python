# Student Grade Evaluator: Input a
# student’s marks in five subjects,
# calculate the average, and assign a
# grade based on the average using ifelif-else. Store marks in a list and use a
# function to compute the average.

def average(student):
    sum =0
    for i in student:
        sum = sum + i
    return sum/len(student)

marks=[]
for i in range(0, 5):
    sj = float(input(f"Enter subject {i+1} marks"))
    marks.append(sj)

mean = average(marks)
print(mean)




