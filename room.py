import json
import os

file_name = "data/rooms.json"

def get_rooms():
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            return json.load(file)
    return []

def save_rooms(rooms):
    with open(file_name, "w") as file:
        json.dump(rooms, file, indent=4)

def show_rooms():
    rooms = get_rooms()

    if len(rooms) == 0:
        print("No rooms found.")
        return

    print("\n===== Room Details =====")

    for room in rooms:
        print("Room No:", room["room_no"])
        print("Type:", room["type"])
        print("Price:", room["price"])
        print("Status:", room["status"])
        print("------------------------")

def available_rooms():
    rooms = get_rooms()

    print("\n===== Available Rooms =====")

    found = False

    for room in rooms:
        if room["status"] == "Available":
            print(
                "Room:", room["room_no"],
                "| Type:", room["type"],
                "| Price:", room["price"]
            )
            found = True

    if found == False:
        print("No rooms are available right now.")

def add_room():
    rooms = get_rooms()

    room_no = input("Enter room number: ")

    for room in rooms:
        if room["room_no"] == room_no:
            print("This room already exists.")
            return

    room_type = input("Enter room type: ")
    price = float(input("Enter room price: "))

    new_room = {
        "room_no": room_no,
        "type": room_type,
        "price": price,
        "status": "Available"
    }

    rooms.append(new_room)
    save_rooms(rooms)

    print("Room added successfully.")

def room_menu():
    while True:
        print("\n===== Room Management =====")
        print("1. Show All Rooms")
        print("2. Show Available Rooms")
        print("3. Add Room")
        print("4. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_rooms()

        elif choice == "2":
            available_rooms()

        elif choice == "3":
            add_room()

        elif choice == "4":
            break

        else:
            print("Invalid choice.")
