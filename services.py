import json
import os

file_name = "data/services.json"

def get_services():
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            return json.load(file)
    return []

def save_services(services):
    with open(file_name, "w") as file:
        json.dump(services, file, indent=4)

def add_service():
    services = get_services()

    service_id = input("Enter service ID: ")
    guest_id = input("Enter guest ID: ")
    service_name = input("Enter service name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per unit: "))

    total = quantity * price

    new_service = {
        "service_id": service_id,
        "guest_id": guest_id,
        "service": service_name,
        "quantity": quantity,
        "price": price,
        "total": total
    }

    services.append(new_service)
    save_services(services)

    print("Service added successfully.")
    print("Service charge:", total)

def show_services():
    services = get_services()

    if len(services) == 0:
        print("No services have been added.")
        return

    print("\n===== Hotel Services =====")

    for service in services:
        print("Service ID:", service["service_id"])
        print("Guest ID:", service["guest_id"])
        print("Service:", service["service"])
        print("Quantity:", service["quantity"])
        print("Price:", service["price"])
        print("Total:", service["total"])
        print("--------------------------")

def service_menu():
    while True:
        print("\n===== Hotel Services =====")
        print("1. Add Service")
        print("2. Show Services")
        print("3. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_service()

        elif choice == "2":
            show_services()

        elif choice == "3":
            break

        else:
            print("Invalid choice.")
