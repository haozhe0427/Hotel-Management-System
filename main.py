"""
Case Study: Hotel Management System
The Hotel Management System manages operations related to hotel bookings, guest/customer management,
and food services through different roles. Each role has specific functionalities to streamline operations. A
ll data is managed using file handling, including adding, reading, updating, and deleting data from text files.
The system operates through a command-line interface with menus customized for each role.

Here are four possible roles within the system, each with its unique functionalities:
1. ADMINISTRATOR
- Add New Rooms: Add details of new rooms (Room number, type, price, availability).
- Remove Rooms: Remove a room from the system by its room number.
- Update Room Information: Edit room details (e.g., price, availability status).
- Generate Reports: Summarize total bookings and room availability.
- View All Data: Display all room and booking information for administrative review.

2. RECEPTIONIST
- Check Room Availability: View available rooms based on type (e.g., Single, Double, Suite).
- Book Room: Record a room booking with guest details (name, contact, room number, duration).
- Cancel Booking: Remove a booking and update room availability.
- Update Guest Details: Edit guest information for an existing booking.
- View All Bookings: Display all current and past bookings.

3. HOTEL GUEST
- View Booking Details: Access booking details (room number, dates, price).
- Cancel Booking: Request to cancel a booking.
- View Menu: Browse the restaurant menu with items, categories, and prices.
- Order Food: Select items from the menu, specify quantity, and place an order.
- View Food Orders: Access the list of current food orders placed for the room.

4. RESTAURANT MANAGER
- Add New Menu Items: Record new dishes to the menu (name, price, category).
- Update Menu Items: Edit details of existing menu items (e.g., price or availability).
- View Menu: Display the current menu with all items and prices.
- Record Food Orders: Record food orders from guests, including room number and items ordered.
- Generate Sales Report: Summarize total sales and most popular dishes.
"""


def dashboard():
    print("==================== Hotel Management System ====================")
    print("Roles:")
    print("1. ADMINISTRATOR")
    print("2. RECEPTIONIST")
    print("3. HOTEL GUEST")
    print("4. RESTAURANT MANAGER")
    print("0. EXIT")
    print("")

def main():
    running = True
    while running:
        dashboard()
        role_Selected = input("Please Select your role: ")

        if role_Selected == "1":  # ADMINISTRATOR
            print("==================== Hotel Management System ====================")
            print("Please Login by username & password")
            administrator_Username = input("Username: ")
            administrator_Password = input("Password: ")
            print("")

            try:
                with open('Account.txt')as file:
                    for line in file:
                        user_Information = []
                        user_Information = line.strip().split(";")
                        username = user_Information[3]
                        password = user_Information[4]

                        if username == administrator_Username and password == administrator_Password:
                            print("Login Successful")
                            print("==================== Hotel Management System (Administrator) ====================")
                            print("1. Add New Rooms")
                            print("2. Remove Rooms")
                            print("3. Update Room Information")
                            print("4. Generate Reports")
                            print("5. View All Data")
                            print("0. Back")
                            print("")
                            option = input("Please Select your option: ")

                            # - Add New Rooms: Add details of new rooms (Room number, type, price, availability).
                            # - Remove Rooms: Remove a room from the system by its room number.
                            # - Update Room Information: Edit room details (e.g., price, availability status).
                            # - Generate Reports: Summarize total bookings and room availability.
                            # - View All Data: Display all room and booking information for administrative review.
                        else:
                            print("Invalid Account. Please try again.")

            except FileNotFoundError:
                print("Can't read Account.txt, Please try again.")


        elif role_Selected == "2": # RECEPTIONIST
            print("==================== Hotel Management System ====================")
            print("Please Login by username & password")
            receptionist_Username = input("Username: ")
            receptionist_Password = input("Password: ")
            print("")

            try:
                with open('Account.txt')as file:
                    for line in file:
                        user_Information = []
                        user_Information = line.strip().split(";")
                        username = user_Information[3]
                        password = user_Information[4]

                        if username == receptionist_Username and password == receptionist_Password:
                            print("Login Successful")
                            print("==================== Hotel Management System (Receptionist) ====================")
                            print("1. Check Room Availability")
                            print("2. Book Room")
                            print("3. Cancel Booking")
                            print("4. Update Guest Details")
                            print("5. View All Bookings")
                            print("0. Back")
                            print("")
                            option = input("Please Select your option: ")
                            return
                            # - Check Room Availability: View available rooms based on type (e.g., Single, Double, Suite).
                            # - Book Room: Record a room booking with guest details (name, contact, room number, duration).
                            # - Cancel Booking: Remove a booking and update room availability.
                            # - Update Guest Details: Edit guest information for an existing booking.
                            # - View All Bookings: Display all current and past bookings.

                    print("Invalid Account. Please try again.")

            except FileNotFoundError:
                print("Can't read Account.txt, Please try again.")


        elif role_Selected == "3": # HOTEL GUEST
            print("==================== Hotel Management System ====================")
            print("Please Login by username & password")
            hotelGuest_Username = input("Username: ")
            hotelGuest_Password = input("Password: ")
            print("")

            try:
                with open('Account.txt')as file:
                    for line in file:
                        user_Information = []
                        user_Information = line.strip().split(";")
                        username = user_Information[3]
                        password = user_Information[4]

                        if username == hotelGuest_Username and password == hotelGuest_Password:
                            print("Login Successful")
                            print("==================== Hotel Management System (Hotel Guest) ====================")
                            print("1. View Booking Details")
                            print("2. Cancel Booking")
                            print("3. View Menu")
                            print("4. Order Food")
                            print("5. View Food Orders")
                            print("0. Back")
                            print("")
                            option = input("Please Select your option: ")
                            return

                            # - View Booking Details: Access booking details (room number, dates, price).
                            # - Cancel Booking: Request to cancel a booking.
                            # - View Menu: Browse the restaurant menu with items, categories, and prices.
                            # - Order Food: Select items from the menu, specify quantity, and place an order.
                            # - View Food Orders: Access the list of current food orders placed for the room.

                    print("Invalid Account. Please try again.")

            except FileNotFoundError:
                print("Can't read Account.txt, Please try again.")

        elif role_Selected == "4": # RESTAURANT MANAGER
            print("==================== Hotel Management System ====================")
            print("Please Login by username & password")
            restaurantManager_Username = input("Username: ")
            restaurantManager_Password = input("Password: ")
            print("")

            try:
                with open('Account.txt')as file:
                    for line in file:
                        user_Information = []
                        user_Information = line.strip().split(";")
                        username = user_Information[3]
                        password = user_Information[4]

                        if username == restaurantManager_Username and password == restaurantManager_Password:
                            print("Login Successful")
                            print("==================== Hotel Management System (Restaurant Manager) ====================")
                            print("1. View New Menu Items")
                            print("2. Update Menu Items")
                            print("3. View Menu")
                            print("4. Record Food Orders")
                            print("5. Generate Sales Report")
                            print("0. Back")
                            print("")
                            option = input("Please Select your option: ")
                            return

                            # - Add New Menu Items: Record new dishes to the menu (name, price, category).
                            # - Update Menu Items: Edit details of existing menu items (e.g., price or availability).
                            # - View Menu: Display the current menu with all items and prices.
                            # - Record Food Orders: Record food orders from guests, including room number and items ordered.
                            # - Generate Sales Report: Summarize total sales and most popular dishes.

                    print("Invalid Account. Please try again.")

            except FileNotFoundError:
                print("Can't read Account.txt, Please try again.")

        elif role_Selected == "0":
            print("==================== Hotel Management System ====================")
            choice = input("Are you sure you want to exit? (Y/N): ")
            if choice.capitalize() == "Y":
                running = False
            elif choice.capitalize() == "N":
                print("Continuing...")
            else:
                print("Invalid Input. Please try again.")

        else:
            print("Invalid Role. Please try again.")

main()