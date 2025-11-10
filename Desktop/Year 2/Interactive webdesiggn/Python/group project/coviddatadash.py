# covid_dashboard.py
import csv
import matplotlib.pyplot as plt

def read_covid_data():
    dates, cases, recoveries = [], [], []
    with open("covid_data.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            dates.append(row[0])
            cases.append(int(row[1]))
            recoveries.append(int(row[2]))
    return dates, cases, recoveries

def plot_covid_trends(dates, cases, recoveries):
    plt.plot(dates, cases, label="Cases", marker='o')
    plt.plot(dates, recoveries, label="Recoveries", marker='x')
    plt.title("COVID-19 Trends")
    plt.xlabel("Date")
    plt.ylabel("Count")
    plt.legend()
    plt.show()

# Example usage
# covid_data.csv -> Date,Cases,Recoveries
# 2025-11-01,120,100
# 2025-11-02,150,130
dates, cases, recoveries = read_covid_data()
plot_covid_trends(dates, cases, recoveries)
