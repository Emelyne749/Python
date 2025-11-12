# student_report_card.py
import matplotlib.pyplot as plt

class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks  # dict: {"Math": 90, "English": 85}

    def average(self):
        return sum(self.marks.values()) / len(self.marks)

    def grade(self):
        avg = self.average()
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'

def save_student(student):
    with open("report_cards.txt", "a") as f:
        f.write(f"Name: {student.name}, Roll No: {student.roll_no}, Average: {student.average():.2f}, Grade: {student.grade()}\n")

def plot_grades(students):
    grades = [s.grade() for s in students]
    plt.hist(grades, bins=5, edgecolor='black')
    plt.title("Grade Distribution")
    plt.xlabel("Grades")
    plt.ylabel("Number of Students")
    plt.show()

# Example usage
students = [
    Student("Alice", 1, {"Math": 85, "English": 90, "Science": 78}),
    Student("Bob", 2, {"Math": 72, "English": 65, "Science": 70})
]

for s in students:
    save_student(s)

plot_grades(students)
