import json
import os

file_name = "data/guests.json"

def get_guests():
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            return json.load(file)
    return []

def save_guests(guests):
    with open(file_name, "w") as file:
        json.dump(guests, file, indent=4)

def add_guest():
    guests = get_guests()

    guest_id = input("Enter guest ID: ")

    for guest in guests:
        if guest["id"] == guest_id:
            print("This guest ID already exists.")
            return

    name = input("Enter guest name: ")
    age = input("Enter age: ")
    gender = input("Enter gender: ")
    phone = input("Enter phone number: ")
    address = input("Enter address: ")

    new_guest = {
        "id": guest_id,
        "name": name,
        "age": age,
        "gender": gender,
        "phone": phone,
        "address": address
    }

    guests.append(new_guest)
    save_guests(guests)

    print("Guest added successfully.")

def show_guests():
    guests = get_guests()

    if len(guests) == 0:
        print("No guest records found.")
        return

    print("\n----- Guest List -----")

    for guest in guests:
        print("ID:", guest["id"])
        print("Name:", guest["name"])
        print("Age:", guest["age"])
        print("Gender:", guest["gender"])
        print("Phone:", guest["phone"])
        print("Address:", guest["address"])
        print("----------------------")

def search_guest():
    guests = get_guests()

    guest_id = input("Enter guest ID to search: ")

    for guest in guests:
        if guest["id"] == guest_id:
            print("\nGuest found!")
            print("Name:", guest["name"])
            print("Age:", guest["age"])
            print("Gender:", guest["gender"])
            print("Phone:", guest["phone"])
            print("Address:", guest["address"])
            return

    print("Guest not found.")

def guest_menu():
    while True:
        print("\n===== Guest Management =====")
        print("1. Add Guest")
        print("2. Show Guests")
        print("3. Search Guest")
        print("4. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_guest()

        elif choice == "2":
            show_guests()

        elif choice == "3":
            search_guest()

        elif choice == "4":
            break

        else:
            print("Please enter a valid choice.")
