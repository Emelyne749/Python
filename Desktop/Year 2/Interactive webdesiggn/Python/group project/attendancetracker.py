# attendance_tracker.py
import csv
import matplotlib.pyplot as plt

def mark_attendance(name, status):
    with open("attendance.csv", "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([name, status])

def calculate_attendance():
    attendance = {}
    with open("attendance.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            name, status = row
            if name not in attendance:
                attendance[name] = {"Present": 0, "Total": 0}
            attendance[name]["Total"] += 1
            if status == "Present":
                attendance[name]["Present"] += 1

    for name, data in attendance.items():
        percent = (data["Present"] / data["Total"]) * 100
        print(f"{name}: {percent:.2f}% attendance")

    return attendance

def plot_attendance(attendance):
    names = list(attendance.keys())
    percentages = [(v["Present"]/v["Total"])*100 for v in attendance.values()]
    plt.bar(names, percentages)
    plt.title("Employee Attendance Percentage")
    plt.xlabel("Employee")
    plt.ylabel("Attendance %")
    plt.show()

# Example usage
mark_attendance("Alice", "Present")
mark_attendance("Bob", "Absent")
attendance = calculate_attendance()
plot_attendance(attendance)
