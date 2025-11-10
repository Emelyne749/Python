# Build a program where users can
# register (username, password) and then
# log in. Use File writing for registration
# and reading for login validation.

import os

if not os.path.exists("users.txt"):
    with open("users.txt", "w") as file:
        pass  # just create an empty file

def register():
    username = input("Enter your username: ")
    password = input("Enter a strong password: ")

    with open("users.txt", "r") as file:
        for line in file:
            uname, pword= line.strip().split(",")
            if uname == username:
                print("Username already exists.")
                return

    with open("users.txt", "a") as file:
        file.write(f"{username},{password}\n")
    print("Successful registration")


def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    with open("users.txt", "r") as file:
        for line in file:
            stored_username, stored_password = line.strip().split(",")
            if stored_username == username and stored_password == password:
                print("Login successful! Welcome,", username)
                return
    print("Invalid username or password.")


while True:
    print("  MENU  ")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")



