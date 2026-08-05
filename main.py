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


def credential_Validation(role_name):
    print("==================== Hotel Management System ====================")
    print("Please Login by username & password")
    input_Username = input("Username: ")
    input_Password = input("Password: ")
    print("")
    try:
        with open('Account.txt') as file:
            for line in file:
                user_Information = line.strip().split(";")
                username = user_Information[3]
                password = user_Information[4]
                userRole = user_Information[5]
                if username == input_Username and password == input_Password:
                    if userRole == role_name:
                        print("login Successful")
                        return True
                    else:
                        print("Invalid role. Please try again")
                        return False
            print("Invalid Account. Please try again.")
            return False
    except FileNotFoundError:
        print("Can't read Account.txt, Please try again.")
        return False


def main():
    mainDashboard_isRunning = True

    while mainDashboard_isRunning:
        dashboard()
        role_Selected = input("Please Select your role: ")

        # ============================================================================================================= #
        # ADMINISTRATOR                                                                                                 #
        # ============================================================================================================= #
        if role_Selected == "1":
            if credential_Validation("Administrator"):
                administratorDashboard_isRunning = True

                while administratorDashboard_isRunning:
                    print("==================== Hotel Management System (Administrator) ====================")
                    print("1. Add New Rooms")
                    print("2. Remove Rooms")
                    print("3. Update Room Information")
                    print("4. Generate Reports")
                    print("5. View All Data")
                    print("0. Back")
                    print("")
                    administrator_Option = input("Please Select your option: ")

                    if administrator_Option == "1":
                        # ============================================================================================= #
                        # Add New Rooms: Add details of new rooms (Room number, type, price, availability).             #
                        # ============================================================================================= #
                        print("1. Add New Rooms")

                    elif administrator_Option == "2":
                        # ============================================================================================= #
                        # Remove Rooms: Remove a room from the system by its room number.                               #
                        # ============================================================================================= #
                        print("2. Remove Rooms")

                    elif administrator_Option == "3":
                        # ============================================================================================= #
                        # Update Room Information: Edit room details (e.g., price, availability status).                #
                        # ============================================================================================= #
                        print("3. Update Room Information")

                    elif administrator_Option == "4":
                        # ============================================================================================= #
                        # Generate Reports: Summarize total bookings and room availability.                             #
                        # ============================================================================================= #
                        print("4. Generate Reports")

                    elif administrator_Option == "5":
                        # ============================================================================================= #
                        # View All Data: Display all room and booking information for administrative review.            #
                        # ============================================================================================= #
                        print("5. View All Data")

                    elif administrator_Option == "0":
                        administratorDashboard_isRunning = False
                        break

                    else:
                        print("Invalid Option. Please try again")

        # ============================================================================================================= #
        # RECEPTIONIST                                                                                                  #
        # ============================================================================================================= #
        elif role_Selected == "2":
            if credential_Validation("Receptionist"):
                receptionistDashboard_isRunning = True

                while receptionistDashboard_isRunning:
                    print("==================== Hotel Management System (Receptionist) ====================")
                    print("1. Check Room Availability")
                    print("2. Book Room")
                    print("3. Cancel Booking")
                    print("4. Update Guest Details")
                    print("5. View All Bookings")
                    print("0. Back")
                    print("")
                    receptionist_Option = input("Please Select your option: ")

                    if receptionist_Option == "1":
                        # ============================================================================================= #
                        # Check Room Availability: View available rooms based on type (e.g., Single, Double, Suite).    #
                        # ============================================================================================= #
                        print("1. Check Room Availability")

                    elif receptionist_Option == "2":
                        # ============================================================================================= #
                        # Book Room: Record a room booking with guest details (name, contact, room number, duration).   #
                        # ============================================================================================= #
                        print("2. Book Room")

                    elif receptionist_Option == "3":
                        # ============================================================================================= #
                        # Cancel Booking: Remove a booking and update room availability.                                #
                        # ============================================================================================= #
                        print("3. Cancel Booking")

                    elif receptionist_Option == "4":
                        # ============================================================================================= #
                        # Update Guest Details: Edit guest information for an existing booking.                         #
                        # ============================================================================================= #
                        print("4. Update Guest Details")

                    elif receptionist_Option == "5":
                        # ============================================================================================= #
                        # View All Bookings: Display all current and past bookings.                                     #
                        # ============================================================================================= #
                        print("5. View All Bookings")

                    elif receptionist_Option == "0":
                        receptionistDashboard_isRunning = False
                        break

                    else:
                        print("Invalid Option. Please try again")

        # ============================================================================================================= #
        # HOTEL GUEST                                                                                                   #
        # ============================================================================================================= #
        elif role_Selected == "3":
            if credential_Validation("Hotel Guest"):
                hotelGuestDashboard_isRunning = True

                while hotelGuestDashboard_isRunning:
                    print("==================== Hotel Management System (Hotel Guest) ====================")
                    print("1. View Booking Details")
                    print("2. Cancel Booking")
                    print("3. View Menu")
                    print("4. Order Food")
                    print("5. View Food Orders")
                    print("0. Back")
                    print("")
                    hotelGuest_Option = input("Please Select your option: ")

                    if hotelGuest_Option == "1":
                        # ============================================================================================= #
                        # View Booking Details: Access booking details (room number, dates, price).                     #
                        # ============================================================================================= #
                        print("1. View Booking Details")

                    elif hotelGuest_Option == "2":
                        # ============================================================================================= #
                        # Cancel Booking: Request to cancel a booking.                                                  #
                        # ============================================================================================= #
                        print("2. Cancel Booking")

                    elif hotelGuest_Option == "3":
                        # ============================================================================================= #
                        # View Menu: Browse the restaurant menu with items, categories, and prices.                     #
                        # ============================================================================================= #
                        print("3. View Menu")

                    elif hotelGuest_Option == "4":
                        # ============================================================================================= #
                        # Order Food: Select items from the menu, specify quantity, and place an order.                 #
                        # ============================================================================================= #
                        print("4. Order Food")

                    elif hotelGuest_Option == "5":
                        # ============================================================================================= #
                        # View Food Orders: Access the list of current food orders placed for the room.                 #
                        # ============================================================================================= #
                        print("5. View Food Orders")

                    elif hotelGuest_Option == "0":
                        hotelGuestDashboard_isRunning = False
                        break

                    else:
                        print("Invalid Option. Please try again")

        # ============================================================================================================= #
        # RESTAURANT MANAGER                                                                                            #
        # ============================================================================================================= #
        elif role_Selected == "4":
            if credential_Validation("Hotel Guest"):
                restaurantManagementDashboard_isRunning = True

                while restaurantManagementDashboard_isRunning:
                    print("==================== Hotel Management System (Restaurant Manager) ====================")
                    print("1. Add New Menu Items")
                    print("2. Update Menu Items")
                    print("3. View Menu")
                    print("4. Record Food Orders")
                    print("5. Generate Sales Report")
                    print("0. Back")
                    print("")
                    restaurantManager_Option = input("Please Select your option: ")

                    if restaurantManager_Option == "1":
                        # ============================================================================================= #
                        # Add New Menu Items: Record new dishes to the menu (name, price, category).                    #
                        # ============================================================================================= #
                        print("1. Add New Menu Items")

                    elif restaurantManager_Option == "2":
                        # ============================================================================================= #
                        # Update Menu Items: Edit details of existing menu items (e.g., price or availability).         #
                        # ============================================================================================= #
                        print("2. Update Menu Items")

                    elif restaurantManager_Option == "3":
                        # ============================================================================================= #
                        # View Menu: Display the current menu with all items and prices.                                #
                        # ============================================================================================= #
                        print("3. View Menu Items")

                    elif restaurantManager_Option == "4":
                        # ============================================================================================= #
                        # Record Food Orders: Record food orders from guests, including room number and items ordered.  #
                        # ============================================================================================= #
                        print("4. Record Food Orders")

                    elif restaurantManager_Option == "5":
                        # ============================================================================================= #
                        # Generate Sales Report: Summarize total sales and most popular dishes.                         #
                        # ============================================================================================= #
                        print("5. Generate Sales Report")

                    elif restaurantManager_Option == "0":
                        restaurantDashboard_isRunning = False
                        break

                    else:
                        print("Invalid Option. Please try again")

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