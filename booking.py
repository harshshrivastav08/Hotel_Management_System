import json
import os

booking_file = "data/bookings.json"
room_file = "data/rooms.json"

def get_bookings():
    if os.path.exists(booking_file):
        with open(booking_file, "r") as file:
            return json.load(file)
    return []

def save_bookings(bookings):
    with open(booking_file, "w") as file:
        json.dump(bookings, file, indent=4)

def get_rooms():
    if os.path.exists(room_file):
        with open(room_file, "r") as file:
            return json.load(file)
    return []

def save_rooms(rooms):
    with open(room_file, "w") as file:
        json.dump(rooms, file, indent=4)

def book_room():
    bookings = get_bookings()
    rooms = get_rooms()

    room_no = input("Enter room number: ")

    selected_room = None

    for room in rooms:
        if room["room_no"] == room_no:
            selected_room = room
            break

    if selected_room is None:
        print("Room not found.")
        return

    if selected_room["status"] == "Occupied":
        print("Sorry, this room is already occupied.")
        return

    booking_id = input("Enter booking ID: ")
    guest_id = input("Enter guest ID: ")
    check_in = input("Enter check-in date (DD-MM-YYYY): ")
    check_out = input("Enter check-out date (DD-MM-YYYY): ")

    booking = {
        "booking_id": booking_id,
        "guest_id": guest_id,
        "room_no": room_no,
        "check_in": check_in,
        "check_out": check_out,
        "status": "Active"
    }

    bookings.append(booking)

    selected_room["status"] = "Occupied"

    save_bookings(bookings)
    save_rooms(rooms)

    print("Room booked successfully.")

def show_bookings():
    bookings = get_bookings()

    if len(bookings) == 0:
        print("No bookings found.")
        return

    print("\n===== Booking Details =====")

    for booking in bookings:
        print("Booking ID:", booking["booking_id"])
        print("Guest ID:", booking["guest_id"])
        print("Room No:", booking["room_no"])
        print("Check-in:", booking["check_in"])
        print("Check-out:", booking["check_out"])
        print("Status:", booking["status"])
        print("---------------------------")

def checkout():
    bookings = get_bookings()
    rooms = get_rooms()

    booking_id = input("Enter booking ID: ")

    for booking in bookings:

        if booking["booking_id"] == booking_id:

            if booking["status"] == "Completed":
                print("This booking is already completed.")
                return

            booking["status"] = "Completed"

            for room in rooms:
                if room["room_no"] == booking["room_no"]:
                    room["status"] = "Available"
                    break

            save_bookings(bookings)
            save_rooms(rooms)

            print("Check-out completed.")
            return

    print("Booking not found.")

def booking_menu():
    while True:
        print("\n===== Booking Management =====")
        print("1. Book Room")
        print("2. Show Bookings")
        print("3. Check-out")
        print("4. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            book_room()

        elif choice == "2":
            show_bookings()

        elif choice == "3":
            checkout()

        elif choice == "4":
            break

        else:
            print("Invalid choice.")
