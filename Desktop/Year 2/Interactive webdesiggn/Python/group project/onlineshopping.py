# shopping_cart_system.py
import csv

class Product:
    def __init__(self, pid, name, price):
        self.pid = pid
        self.name = name
        self.price = price

class Cart:
    def __init__(self):
        self.items = {}  # {product_id: quantity}

    def add_item(self, product, qty):
        self.items[product.pid] = self.items.get(product.pid, 0) + qty
        print(f"Added {qty}x {product.name} to cart.")

    def remove_item(self, product):
        if product.pid in self.items:
            del self.items[product.pid]
            print(f"Removed {product.name} from cart.")
        else:
            print("Item not in cart.")

    def calculate_total(self, products, tax_rate=0.1):
        total = 0
        for pid, qty in self.items.items():
            price = products[pid].price
            total += price * qty
        tax = total * tax_rate
        return total + tax

    def save_receipt(self, products, total):
        with open("order_receipts.csv", "a", newline='') as f:
            writer = csv.writer(f)
            for pid, qty in self.items.items():
                product = products[pid]
                writer.writerow([product.name, qty, product.price, total])
        print("Receipt saved to order_receipts.csv")

# Example usage
products = {
    1: Product(1, "Laptop", 1200),
    2: Product(2, "Mouse", 25),
    3: Product(3, "Keyboard", 45),
    4: Product(4, "Monitor", 200)
}

cart = Cart()
cart.add_item(products[1], 1)
cart.add_item(products[2], 2)
total = cart.calculate_total(products)
print(f"Total with tax: ${total:.2f}")
cart.save_receipt(products, total)
