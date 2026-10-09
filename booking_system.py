from datetime import datetime
#Dictionary for activity prices.
prices = {"Yoga": 10, "Boxing": 15, "Spin": 12}
# Module 1: Read bookings from the file and keep only valid ones
def load_bookings():
    valid_bookings = []
    with open("bookings.txt") as file:
        for line in file:
            parts = line.strip().split(",")
            #here we check whether the ID is a digit
            if parts[0].isdigit():
                #check whether the date and time is correct
                try:
                    datetime.strptime(parts[3], "%Y-%m-%d")
                    print("Valid:", parts)
                    valid_bookings.append(parts)
                except ValueError:
                    print("Invalid date and time.")
            else:
                print("Invalid ID", parts)
    return valid_bookings
# Module 2: calculating totals for the gym and each activity.
def calculate_fees(bookings):
    total = 0
    for booking in bookings:
        print(booking[1], prices[booking[2]])
        total = total + prices[booking[2]]
    print("Total:", total)
    return total
#Module 3 :displaying our bookings data in a table.
def print_report(bookings, total):
    print("===== GYM BOOKING REPORT =====")
    print(f"{'ID':<6}{'Name':<10}{'Class':<10}{'Date':<12}{'Fee':<5}")
    for booking in bookings:
        print(f"{booking[0]:<6}{booking[1]:<10}{booking[2]:<10}{booking[3]:<12}{prices[booking[2]]}")
    print("Total revenue:", total)
#Module 4 : Displaying options for booking,fees,reports or finish
def main_menu():
    bookings=[]
    total =0
    while True:
        print("1. Load bookings")
        print("2. Calculate fees")
        print("3. Show report")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == "4":
            print("Goodbye!")
            break
        elif choice == "1":
               bookings = load_bookings()
        elif choice == "2":
               total = calculate_fees(bookings)
        elif choice == "3":
            print_report(bookings, total)
        else:
            print("Invalid option, please choose 1-4.")
main_menu()