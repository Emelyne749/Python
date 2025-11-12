# restaurant_system.py
import csv

menu = {
    "Burger": 5.0,
    "Pizza": 8.5,
    "Soda": 2.0,
    "Fries": 3.0
}

def show_menu():
    print("\n--- Menu ---")
    for item, price in menu.items():
        print(f"{item}: ${price:.2f}")

def take_order():
    order = {}
    show_menu()
    while True:
        item = input("Enter item to order (or 'done' to finish): ")
        if item.lower() == "done":
            break
        if item in menu:
            qty = int(input(f"Enter quantity for {item}: "))
            order[item] = order.get(item, 0) + qty
        else:
            print("Item not found.")
    return order

def calculate_bill(order):
    total = sum(menu[item] * qty for item, qty in order.items())
    print(f"Total Bill: ${total:.2f}")
    with open("sales.csv", "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([order, total])
    return total

# Example usage
order = take_order()
calculate_bill(order)
