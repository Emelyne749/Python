# library_system.py
import csv

class Book:
    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

class Library:
    def __init__(self, filename="library.csv"):
        self.filename = filename

    def add_book(self, book):
        with open(self.filename, "a", newline='') as f:
            writer = csv.writer(f)
            writer.writerow([book.title, book.author, book.isbn, book.available])

    def view_books(self):
        print("\n--- Library Books ---")
        with open(self.filename, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                print(f"Title: {row[0]}, Author: {row[1]}, ISBN: {row[2]}, Available: {row[3]}")

    def borrow_book(self, isbn):
        rows = []
        borrowed = False
        with open(self.filename, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if row[2] == isbn and row[3] == "True":
                    row[3] = "False"
                    borrowed = True
                rows.append(row)
        with open(self.filename, "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerows(rows)
        if borrowed:
            print("Book borrowed successfully.")
        else:
            print("Book not available or ISBN not found.")

# Example usage
library = Library()
library.add_book(Book("Python Basics", "John Doe", "001"))
library.add_book(Book("Data Science 101", "Jane Smith", "002"))
library.view_books()
library.borrow_book("001")
library.view_books()
