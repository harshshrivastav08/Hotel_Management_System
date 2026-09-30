from guest import guest_menu
from room import room_menu
from booking import booking_menu
from services import service_menu
from billing import billing_menu

def main():

    while True:

        print("\n")
        print("======================================")
        print("       HOTEL MANAGEMENT SYSTEM")
        print("======================================")
        print("1. Guest Management")
        print("2. Room Management")
        print("3. Booking Management")
        print("4. Hotel Services")
        print("5. Billing")
        print("6. Exit")
        print("======================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            guest_menu()

        elif choice == "2":
            room_menu()

        elif choice == "3":
            booking_menu()

        elif choice == "4":
            service_menu()

        elif choice == "5":
            billing_menu()

        elif choice == "6":
            print("Thank you for using the Hotel Management System.")
            break

        else:
            print("Invalid choice. Please try again.")

main()
