# expense_tracker.py
import csv
import matplotlib.pyplot as plt

def add_expense(amount, category, date):
    with open("expenses.csv", "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([amount, category, date])

def summarize_expenses():
    summary = {}
    with open("expenses.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            amount, category, _ = float(row[0]), row[1], row[2]
            summary[category] = summary.get(category, 0) + amount
    return summary

def plot_expenses(summary):
    categories = summary.keys()
    amounts = summary.values()
    plt.bar(categories, amounts)
    plt.title("Category-wise Spending")
    plt.xlabel("Category")
    plt.ylabel("Amount Spent")
    plt.show()

# Example usage
add_expense(50, "Food", "2025-11-10")
add_expense(30, "Transport", "2025-11-10")
summary = summarize_expenses()
plot_expenses(summary)
