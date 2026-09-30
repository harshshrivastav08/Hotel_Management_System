Hotel Management System

This is a simple Hotel Management System I built with Python. It runs entirely in the terminal—no graphics, no internet required, and no database setup. Everything saves locally to JSON files, so all your data stays in your project folder.

I broke the project into a few files to keep things tidy and readable. Each file handles its own piece of the system.

What it does

- Add and search for guests
- See which rooms are available (or not)
- Book rooms and check guests out
- Track extras like food, laundry, and other services
- Calculate charges for rooms and those services
- Create and view bills

Project structure

Hotel_Management_System/
├── main.py
├── guest.py
├── room.py
├── booking.py
├── services.py
├── billing.py
└── data/
    ├── guests.json
    ├── rooms.json
    ├── bookings.json
    ├── services.json
    └── bills.json

What’s in each file

- main.py — Shows the main menu and directs you to the right section.
- guest.py — Lets you add guests, search for them, and list their info.
- room.py — Manages room details and checks what’s available.
- booking.py — Handles room bookings and the checkout process.
- services.py — Logs extras used by guests, like meals or laundry.
- billing.py — Figures out room and service charges, adds tax, and creates the bill.
- data/ — Keeps all the records in JSON format.

Requirements

- Python 3
- No extra packages

The whole project relies on Python’s built-in json, os, and datetime modules, so there’s nothing to install.

How to run it

1. Make sure Python 3 is installed on your system.
2. Put main.py, guest.py, room.py, booking.py, services.py, and billing.py in one folder.
3. Inside that folder, make a directory called data.
4. In the data folder, create these files: guests.json, bookings.json, services.json, and bills.json. Just put [] in each to start.
5. For rooms.json, you can also start with [] and use the program to add new rooms.
6. Open your terminal in the project folder and run:

   python main.py

Depending on your setup, you might need python3 instead of python.

How billing works

When you check a guest out, the system figures out the bill: room price times days stayed, plus charges for any extra services. After that, it adds 5% tax.

Room charge = Room price × Number of days
Subtotal = Room charge + Service charges
Tax = Subtotal × 5%
Final bill = Subtotal + Tax

Python concepts

This project brings together all sorts of Python basics: functions, loops, conditionals, lists, dictionaries, modules, file handling, JSON, and simple math. For billing, I used datetime to figure out exactly how long each stay lasted.

Some extra notes

- All data stays local in JSON files.
- Think of this as a demo or learning tool, not something for an actual hotel.
- There’s no web-based booking, payment gateway, database, or fancy interface—just the basics.
- The tax rate is currently set at a flat 5%.

Ideas for the future

Here’s what you could add next: input validation, admin login, discounts, receipt printing, or even switch to a real database.

Why I built this

I wanted to get hands-on with Python by creating something that deals with real-world hotel tasks. Breaking things up into modules also gave me a better idea of how different parts of a Python app work together.
