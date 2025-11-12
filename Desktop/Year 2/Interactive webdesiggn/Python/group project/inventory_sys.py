# inventory_system.py
import csv

class Product:
    def __init__(self, product_id, name, quantity, price):
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.price = price

def add_product(product):
    with open("inventory.csv", "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([product.product_id, product.name, product.quantity, product.price])

def view_inventory():
    with open("inventory.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(f"ID: {row[0]}, Name: {row[1]}, Qty: {row[2]}, Price: {row[3]}")

# Example usage
p1 = Product(1, "Laptop", 10, 1200)
p2 = Product(2, "Mouse", 50, 20)
add_product(p1)
add_product(p2)
view_inventory()
