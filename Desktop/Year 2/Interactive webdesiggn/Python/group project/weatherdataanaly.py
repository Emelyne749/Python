# weather_analyzer.py
import csv
import matplotlib.pyplot as plt

def read_weather_data():
    data = []
    with open("weather.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            day, temp = row[0], float(row[1])
            data.append((day, temp))
    return data

def average_temperature(data):
    temps = [t for _, t in data]
    return sum(temps) / len(temps)

def plot_temperature(data):
    days = [d for d, _ in data]
    temps = [t for _, t in data]
    plt.plot(days, temps, marker='o')
    plt.title("Daily Temperature Trend")
    plt.xlabel("Day")
    plt.ylabel("Temperature (°C)")
    plt.show()

# Example usage
# weather.csv -> Day,Temperature
# Monday,28
# Tuesday,30
# Wednesday,29
data = read_weather_data()
print("Average Temperature:", average_temperature(data))
plot_temperature(data)
