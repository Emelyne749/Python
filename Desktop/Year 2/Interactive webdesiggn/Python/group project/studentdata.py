# student_data_system.py
import csv
import matplotlib.pyplot as plt

class Student:
    def __init__(self, name, id, marks):
        self.name = name
        self.id = id
        self.marks = marks  # dict of subject: score

    def average(self):
        return sum(self.marks.values()) / len(self.marks)

def save_student(student):
    with open("student_data.csv", "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([student.name, student.id, student.marks, student.average()])

def read_students():
    students = []
    with open("student_data.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            students.append((row[0], float(row[3])))
    return students

def plot_performance(students):
    names = [s[0] for s in students]
    averages = [s[1] for s in students]
    plt.bar(names, averages)
    plt.title("Student Performance")
    plt.xlabel("Name")
    plt.ylabel("Average Marks")
    plt.show()

# Example usage
s1 = Student("Alice", 101, {"Math": 85, "English": 90, "Science": 88})
s2 = Student("Bob", 102, {"Math": 70, "English": 75, "Science": 68})
save_student(s1)
save_student(s2)
students = read_students()
plot_performance(students)
