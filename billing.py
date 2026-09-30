import json
import os
from datetime import datetime

booking_file = "data/bookings.json"
room_file = "data/rooms.json"
service_file = "data/services.json"
bill_file = "data/bills.json"

def read_file(file_name):
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            return json.load(file)
    return []

def save_bills(bills):
    with open(bill_file, "w") as file:
        json.dump(bills, file, indent=4)

def generate_bill():
    bookings = read_file(booking_file)
    rooms = read_file(room_file)
    services = read_file(service_file)
    bills = read_file(bill_file)

    booking_id = input("Enter booking ID: ")

    booking = None

    for item in bookings:
        if item["booking_id"] == booking_id:
            booking = item
            break

    if booking is None:
        print("Booking not found.")
        return

    room_price = 0

    for room in rooms:
        if room["room_no"] == booking["room_no"]:
            room_price = room["price"]
            break

    try:
        start_date = datetime.strptime(
            booking["check_in"], "%d-%m-%Y"
        )

        end_date = datetime.strptime(
            booking["check_out"], "%d-%m-%Y"
        )

        days = (end_date - start_date).days

        if days <= 0:
            days = 1

    except ValueError:
        print("Please enter the date in DD-MM-YYYY format.")
        return

    room_charge = room_price * days

    service_charge = 0

    for service in services:
        if service["guest_id"] == booking["guest_id"]:
            service_charge += service["total"]

    subtotal = room_charge + service_charge

    tax = subtotal * 0.05

    total = subtotal + tax

    bill = {
        "bill_id": "B" + str(len(bills) + 1),
        "booking_id": booking_id,
        "guest_id": booking["guest_id"],
        "room_charge": room_charge,
        "service_charge": service_charge,
        "tax": tax,
        "total": total
    }

    bills.append(bill)
    save_bills(bills)

    print("\n========== HOTEL BILL ==========")
    print("Booking ID:", booking_id)
    print("Room charges:", room_charge)
    print("Service charges:", service_charge)
    print("Tax:", tax)
    print("-------------------------------")
    print("Total amount:", total)
    print("================================")

def show_bills():
    bills = read_file(bill_file)

    if len(bills) == 0:
        print("No bills found.")
        return

    print("\n===== Previous Bills =====")

    for bill in bills:
        print("Bill ID:", bill["bill_id"])
        print("Booking ID:", bill["booking_id"])
        print("Guest ID:", bill["guest_id"])
        print("Room charges:", bill["room_charge"])
        print("Service charges:", bill["service_charge"])
        print("Tax:", bill["tax"])
        print("Total:", bill["total"])
        print("--------------------------")

def billing_menu():
    while True:
        print("\n===== Billing Management =====")
        print("1. Generate Bill")
        print("2. Show Bills")
        print("3. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            generate_bill()

        elif choice == "2":
            show_bills()

        elif choice == "3":
            break

        else:
            print("Invalid choice.")
