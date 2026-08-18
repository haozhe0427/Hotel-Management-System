from datetime import date, timedelta
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


class User:
    def __init__(self, account_id, name, phoneNumber, userName, password, role):
        self.account_id  = account_id
        self.name        = name
        self.phoneNumber = phoneNumber
        self.userName    = userName
        self.password    = password
        self.role        = role


# ===================================================================================================================== #
#                                                   Main Dashboard                                                      #
# ===================================================================================================================== #
def dashboard():
    print("==================== Hotel Management System ====================")
    print("Roles:")
    print("1. ADMINISTRATOR")
    print("2. RECEPTIONIST")
    print("3. HOTEL GUEST")
    print("4. RESTAURANT MANAGER")
    print("0. EXIT")
    print("")


# ===================================================================================================================== #
#                                               Credential Validation                                                   #
# ===================================================================================================================== #
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
                user = User(user_Information[0], user_Information[1], user_Information[2],
                            user_Information[3], user_Information[4], user_Information[5])
              # user = User(account_id, name, phoneNumber, userName, password, role)

                if input_Username == user.userName and input_Password == user.password:
                    if user.role == role_name:
                        print("login Successful")
                        return user
                    else:
                        print("Invalid role. Please try again")
                        return None

            print("Invalid Account. Please try again.")
            return None
    except FileNotFoundError:
        print("Can't read Account.txt, Please try again.")
        return None



# ===================================================================================================================== #
#                                              ADMINISTRATOR FUNCTIONS                                                  #
# ===================================================================================================================== #
def Add_New_Rooms():
    print("")
    print("==================== Add New Rooms ====================")
    print("")
    # Step 1: Enter New Room Number
    new_RoomNumber = input("Please enter new room number: ")
    try:
        with open('Rooms.txt') as file:
            for line in file:
                room_information = line.strip().split(";")

                #  new_RoomNumber == roomNumber (in Rooms.txt)
                if new_RoomNumber == room_information[0]:
                    print("Room Number Already Exists")
                    return
                if not new_RoomNumber.isnumeric():
                    print("Invalid room number. Please try again.")
                    return

    except FileNotFoundError:
        print("Can't read Rooms.txt, Please try again.")

    # Step 2: Select Room Type
    roomType_Option = input("Please Select your room type (1. Single / 2. Double / 3. Suite): ")
    if   roomType_Option == "1": roomType = "Single"
    elif roomType_Option == "2": roomType = "Double"
    elif roomType_Option == "3": roomType = "Suite"
    else:
        print("Invalid room type. Please try again.")
        return

    # Step 3: Enter Room Price
    roomPrice = input("Please enter room price: RM")
    if not roomPrice.isnumeric():
        print("Invalid room price. Please try again.")
        return
    try:
        with open('Rooms.txt', 'a') as file:
            file.write(
                new_RoomNumber + ";" + roomType + ";RM "+ roomPrice + ";Yes\n"
            )
    except FileNotFoundError:
        print("Can't read Rooms.txt, Please try again.")
    print("\nRoom " + new_RoomNumber + " added successfully.")


def Remove_Rooms():
    print("")
    print("==================== Remove Rooms ====================")
    print("")
    roomNumber_ToDelete = input("Please enter room number to delete: ")

    if roomNumber_ToDelete == "":
        print("Room number cannot be empty. Please try again.")
        return

    updated_Lines = []
    room_Found    = 0

    try:
        with open('Rooms.txt') as file:
            for line in file:
                room_Information = line.strip().split(";")

                #  roomNumber_ToDelete == roomNumber (in Rooms.txt)
                if roomNumber_ToDelete == room_Information[0]:
                    room_Found += 1
                    updated_Lines.append('')
                else: updated_Lines.append(line)

    except FileNotFoundError:
        print("Can't read Rooms.txt, Please try again.")
        return

    if room_Found == 0:
        print("Room " + roomNumber_ToDelete + " not found.")
        return

    try:
        with open('Rooms.txt', 'w') as file:
            file.writelines(updated_Lines)
        print("Room " + roomNumber_ToDelete + " removed successfully.")
    except FileNotFoundError:
        print("Can't read Rooms.txt, Please try again.")


def Update_Room_Information():
    print("==================== Update Room Information =====================")
    roomNumber_ToUpdate = input("Please enter room number to update: ").strip()

    if roomNumber_ToUpdate == "":
        print("Room number cannot be empty. Please try again.")
        return

    updated_Lines = []
    room_Found    = 0

    try:
        with open('Rooms.txt') as file:
            for line in file:
                room_Information = line.strip().split(";")
                roomNumber       = room_Information[0]
                roomType         = room_Information[1]
                roomPrice        = room_Information[2]
                roomAvailability = room_Information[4]

                if roomNumber == roomNumber_ToUpdate:
                    room_Found += 1

                    while True:
                        print("")
                        print("Room Number: "  + roomNumber)
                        print("Room Type: "    + roomType)
                        print("Room Price: "   + roomPrice)
                        print("Availability: " + roomAvailability)
                        print("")
                        print("1. Room Type")
                        print("2. Room Price")
                        print("3. Switch Room Availability")
                        print("0. Exit / Finish")
                        updateOption = input("Please select a room " + roomNumber_ToUpdate + " information to update: ")

                        if updateOption   == "1": roomType  = input("Please enter new room type: ")
                        elif updateOption == "2": roomPrice = input("Please enter new room price: RM ")
                        elif updateOption == "3":
                            if roomAvailability == "Yes":
                                roomAvailability = "No"
                            else:
                                roomAvailability = "Yes"
                        elif updateOption == "0": break
                        else: print("Invalid option. Please try again.")
                    updated_Lines.append(roomNumber_ToUpdate + ";" + roomType + ";RM " + roomPrice + ";" + roomAvailability + "\n")
                else:
                    updated_Lines.append(line)
    except FileNotFoundError:
        print("Can't read Rooms.txt, Please try again.")
        return

    if room_Found == 0:
        print("Room " + roomNumber_ToUpdate + " does not exist. Please try again.")
        return

    try:
        with open('Rooms.txt', 'w') as file:
            file.writelines(updated_Lines)
        print("Room " + roomNumber_ToUpdate + " updated successfully.")
    except FileNotFoundError:
        print("Can't read Rooms.txt, Please try again.")


def View_All_Data():
    print("==================== View All Data ====================")
    print("All Rooms")
    try:
        with open('Rooms.txt') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("Can't read Rooms.txt, Please try again.")
    print("")

    print("Booking Information")
    try:
        with open('Booking.txt') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("Can't read Booking.txt, Please try again.")
    print("")



# ===================================================================================================================== #
#                                           RECEPTIONIST FUNCTIONS                                                      #
# ===================================================================================================================== #
def Check_Room_Availability():
    print("==================== Check Room Availability ====================")
    try:
        with open('Rooms.txt') as file:
            for line in file:
                room_Information = line.strip().split(";")
                roomAvailability = room_Information[3]

                if roomAvailability == "Yes": print(line.strip())
            print("")
    except FileNotFoundError:
        print("Can't read Rooms.txt, Please try again.")


def View_Booking_Request():
    print("")
    print("==================== View Booking Request ====================")
    print("")
    updated_Lines   = []
    BookingID_Found = 0

    try:
        with open('Booking.txt') as file:
            for line in file:
                booking_Information = line.strip().split(";")
                status              = booking_Information[6]

                if status == "Pending":
                    print(line.strip())
                else:
                    print("BLANK")
                    return
    except FileNotFoundError:
            print("Can't read Booking.txt, Please try again.")

    try:
        with open('Booking.txt') as file:
            for line in file:
                booking_Information = line.strip().split(";")
                bookingID           = booking_Information[0]
                roomNumber          = booking_Information[1]
                roomType            = booking_Information[2]
                guestName           = booking_Information[3]
                checkInDate         = booking_Information[4]
                checkOutDate        = booking_Information[5]

                BookingID_Selected = input("Please enter booking ID (press 0 to cancel): ")
                if BookingID_Selected == "":
                    print("Booking ID cannot be empty. Please try again.")

                elif BookingID_Selected != bookingID:
                    print("Booking ID " + bookingID + " does not exist. Please try again.")

                else:
                    BookingID_Found += 1
                    print("Booking ID: " + bookingID)
                    new_status = input("Please enter new status (0.Back / 1.Approved / 2.Rejected): ")

                    if new_status == "":
                        print("Please enter new status")

                    elif new_status == "1":
                        updated_Lines.append(
                            bookingID + ";" + roomNumber + ";" + roomType + ";" +
                            guestName + ";" + checkInDate + ";" + checkOutDate +
                            ";Approved" + "\n"
                        )
                    elif new_status == "2":
                        updated_Lines.append(
                            bookingID + ";" + roomNumber + ";" + roomType + ";" +
                            guestName + ";" + checkInDate + ";" + checkOutDate +
                            ";Rejected" + "\n"
                        )
                    else:
                        updated_Lines.append(line)

    except FileNotFoundError:
        print("Can't read Booking.txt, Please try again.")

    if BookingID_Found == 0:
        print("Booking " + bookingID + " does not exist. Please try again.")
        return

    try:
        with open('Booking.txt', 'w') as file:
            file.writelines(updated_Lines)
        print("Booking " + bookingID + " status updated successfully.")
    except FileNotFoundError:
        print("Can't read Booking.txt, Please try again.")


def View_Cancel_Booking_Request():
    print("")
    print("==================== View Cancel Booking Request =====================")
    print("")
    updated_Lines = []
    BookingID_Found = 0

    try:
        with open('Booking.txt') as file:
            for line in file:
                bookingInformation = line.strip().split(";")
                status             = bookingInformation[6]

                if status == "Request Cancel":
                    print(line.strip())
                else:
                    print("BLANK")
                    return
    except FileNotFoundError:
        print("Can't read Booking.txt, Please try again.")

    try:
        with open('Booking.txt') as file:
            for line in file:
                booking_Information = line.strip().split(";")
                bookingID           = booking_Information[0]
                roomNumber          = booking_Information[1]
                roomType            = booking_Information[2]
                guestName           = booking_Information[3]
                checkInDate         = booking_Information[4]
                checkOutDate        = booking_Information[5]

                BookingID_Selected = input("Please enter booking ID to approve cancel booking (press 0 to cancel): ")
                if BookingID_Selected == "":
                    print("Booking ID cannot be empty. Please try again.")
                    return

                if BookingID_Selected == bookingID:
                    BookingID_Found += 1
                    updated_Lines.append(bookingID + ";" + roomNumber + ";" + roomType + ";" +
                                         guestName + ";" + checkInDate + ";" + checkOutDate + ";" +
                                         "Cancelled")
                else:
                    updated_Lines.append(line)
    except FileNotFoundError:
        print("Can't read Booking.txt, Please try again.")

    if BookingID_Found == 0:
        print("Booking " + bookingID + " does not exist. Please try again.")
        return

    try:
        with open('Booking.txt', 'w') as file:
            file.writelines(updated_Lines)
        print("Booking " + bookingID + " status updated successfully.")
    except FileNotFoundError:
        print("Can't read Booking.txt, Please try again.")


def View_All_Booking():
    print("==================== View Booking ====================")
    try:
        with open('Booking.txt') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("Can't read Booking.txt, Please try again.")



# ===================================================================================================================== #
#                                               HOTEL GUEST FUNCTIONS                                                   #
# ===================================================================================================================== #
def View_Booking_Details(user):
    print("==================== View Booking Details ====================")
    try:
        with open('Booking.txt') as file:
            for line in file:
                booking_Information = line.strip().split(";")
                guestName           = booking_Information[3]

                if guestName == user.name: print(line.strip())
    except FileNotFoundError:
        print("Can't read Booking.txt, Please try again.")


def Booking_Room(user):
    print("==================== Booking Room ====================")
    Check_Room_Availability()
    roomNumber_ToBooking = input("Please enter room number to booking (press 0 to cancel): ")

    if roomNumber_ToBooking == "":
        print("Room number cannot be empty. Please try again.")
        return

    if roomNumber_ToBooking == "0": return

    updated_Lines       = []
    booking_Information = []
    room_Found          = 0

    try:
        with open('Rooms.txt') as file:
            for line in file:
                room_Information = line.strip().split(";")
                roomNumber       = room_Information[0]
                roomType         = room_Information[1]
                roomPrice        = room_Information[2]
                roomAvailability = room_Information[3]

                if roomNumber != roomNumber_ToBooking:
                    updated_Lines.append(line)
                    continue
                else:
                    if roomAvailability == "No":
                        print("Room " + roomNumber_ToBooking + " has already been booked.")
                        return
                    else:
                        room_Found += 1
                        roomAvailability = "No"
                        updated_Lines.append(roomNumber + ";" + roomType + ";" +
                                             roomPrice + ";" + roomAvailability + "\n")

                        BookingID   = "B" + BookingID_Generator("B")
                        duration = input("Please enter duration (days): ")

                        if duration == "":
                            print("Duration cannot be empty. Please try again.")
                            return

                        elif not duration.isnumeric():
                            print("Invalid duration. Please try again.")
                            return

                        else:
                            duration = int(duration)
                            if duration == 0:
                                print("Invalid duration. Please try again.")
                                return

                            checkInDate  = date.today()
                            checkOutDate = checkInDate + timedelta(days = duration)

                        booking_Information.append(BookingID + ";" + roomNumber + ";" + roomType + ";" +
                                                   user.name + ";" + str(checkInDate) + ";" + str(checkOutDate) + ";" +
                                                   "Pending")
    except FileNotFoundError:
        print("Can't read Rooms.txt, Please try again.")

    if room_Found == 0:
        print("Room " + roomNumber_ToBooking + " does not exist. Please try again.")
        return

    try:
        with open('Rooms.txt', 'w') as file:
            file.writelines(updated_Lines)
        print("Room " + roomNumber_ToBooking + " booking successfully.")
    except FileNotFoundError:
        print("Can't read Rooms.txt, Please try again.")

    try:
        with open('Booking.txt', 'a') as file:
            file.writelines(booking_Information)
    except FileNotFoundError:
        print("Can't read Booking.txt, Please try again.")


def Cancel_Booking(user):
    print("==================== Cancel Booking ======================")
    updated_Lines = []
    guestName_Found = 0

    try:
        with open('Booking.txt') as file:
            for line in file:
                booking_Information = line.strip().split(";")
                BookingID           = booking_Information[0]
                roomNumber          = booking_Information[1]
                roomType            = booking_Information[2]
                guestName           = booking_Information[3]
                checkInDate         = booking_Information[4]
                checkOutDate        = booking_Information[5]

                if guestName == user.name:
                    guestName_Found += 1
                    print(line.strip())
                    print("")

                BookingID_ToCancel = input("Please enter BookingID to cancel(press 0 to exit): ")

                if BookingID_ToCancel == "":
                    print("BookingID cannot be empty. Please try again.")
                    return

                if BookingID_ToCancel == "0":
                    print("Invalid BookingID. Please try again.")
                    return

                if BookingID_ToCancel == BookingID:
                    status = "Request Cancel"
                    updated_Lines.append(BookingID + ";" + roomNumber + ";" + roomType + ";" +
                                               user.name + ";" + str(checkInDate) + ";" + str(checkOutDate) + ";" +
                                               status + "\n")
                else:
                    updated_Lines.append(line)
    except FileNotFoundError:
        print("Can't read Booking.txt, Please try again.")

    if guestName_Found == 0:
        print("Empty Room Booking")
        return

    try:
        with open('Booking.txt', 'w') as file:
            file.writelines(updated_Lines)
        print("Booking " + BookingID + " status updated to request cancel successfully.")
    except FileNotFoundError:
        print("Can't read Booking.txt, Please try again.")


def BookingID_Generator(prefix):
    max_BookingNumber = 0
    try:
        with open('Booking.txt') as file:
            for line in file:
                Booking_Information = line.strip().split(";")
                BookingID           = Booking_Information[0]

                if BookingID.startswith(prefix):
                    current_BookingNumber = int(BookingID.split(prefix)[1])

                    if current_BookingNumber > max_BookingNumber:
                        max_BookingNumber = current_BookingNumber
    except FileNotFoundError:
            print("Can't read Booking.txt, Please try again.")

    return str(max_BookingNumber + 1).zfill(6)


def View_Menu():
    print("")
    print("==================== View Menu ====================")
    try:
        with open('Menu.txt') as file:
            for line in file:
                MenuItem_Information = line.strip().split(",")
                MenuType             = MenuItem_Information[3]

                if MenuType   == "Mains"     : print(line.strip()) # Display Mains
                elif MenuType == "Appetizers": print(line.strip()) # Display Appetizers
                elif MenuType == "Desserts"  : print(line.strip()) # Display Desserts
                elif MenuType == "Beverages" : print(line.strip()) # Display Beverages

            print("End of Menu")
            print("")
    except FileNotFoundError:
        print("Can't read Menu.txt, Please try again.")


def Order_Food(user):
    while True:
        print("")
        print("==================== Order Food ====================")
        print("**Cancel Order = 0, Finish Order = 1")
        SelectedMenuItem_ID = input("Please enter Menu Item ID to order: ")

        Ordered_MenuItem = []
        MenuItem_Found   = 0

        try:
            with open('Menu.txt') as file:
                for line in file:
                    MenuItem_Information = line.strip().split(",")
                    MenuItem_ID          = MenuItem_Information[0]
                    MenuItem_Name        = MenuItem_Information[1]
                    MenuItem_Price       = MenuItem_Information[2]

                    if SelectedMenuItem_ID == MenuItem_ID:
                        MenuItem_Found += 1
                        Ordered_MenuItem.append(MenuItem_ID + "," +
                                                MenuItem_Name + "," +
                                                MenuItem_Price + "," +
                                                user.name + "\n")
        except FileNotFoundError:
            print("Can't read Menu.txt, Please try again.")

        if SelectedMenuItem_ID == "":
            print("Please enter Menu Item ID. Please try again.")
            print("")
            continue

        elif SelectedMenuItem_ID == "0":
            print("")
            break

        elif SelectedMenuItem_ID == "1":
            MenuItem_Found += 1
            print("")
            print("==================== Your cart ====================")
            try:
                with open('OrderedMenuItem.txt') as file:
                    for line in file:
                        print(line.strip())
                    break
            except FileNotFoundError:
                print("Can't read OrderedMenuItem.txt, Please try again.")

        if MenuItem_Found == 0:
            print("Menu Item " + MenuItem_ID + " does not exist. Please try again.")
            return

        try:
            with open('OrderedMenuItem.txt', 'a') as file:
                file.writelines(Ordered_MenuItem)
            print("Menu Item has been moved to cart.")
        except FileNotFoundError:
            print("Can't read Menu.txt, Please try again.")



# ===================================================================================================================== #
#                                           RESTAURANT MANAGER FUNCTIONS                                                #
# ===================================================================================================================== #
def Add_Memu_Items():
    print("==================== Add Menu Item ====================")
    print("1. Add New Mains")
    print("2. Add New Appetizers")
    print("3. Add New Desserts")
    print("4. Add New Beverages")

    # 1. Menu Number
    newMenuType = input("Please enter new Menu Item Type: ")
    prefix_map = {"1": "M",
                  "2": "A",
                  "3": "D",
                  "4": "B"}

    if newMenuType not in prefix_map:
        print("Invalid Menu Item Type. Please try again.")
        return

    prefix         = prefix_map[newMenuType]
    new_MenuItemID = prefix + MenuID_Generator(prefix)
    print("new Menu Item ID: " + new_MenuItemID)

    # 2. Input new Menu Item
    newMenuName = input("Please enter new Menu Item Name: ")
    if newMenuName == "":
        print("Please enter Menu Item Name.")
        return

    # 3. Input Menu Price
    menuPrice = input("Please enter menu price: RM")
    if not menuPrice.isnumeric():
        print("Invalid menu price. Please try again.")
        return

    # 4. Input Menu Type
    menuType_Option = input("Please Select your menu type (1. Mains / 2. Appetizers / 3. Desserts / 4. Beverages): ")
    if menuType_Option   == "1": menuType = "Mains"
    elif menuType_Option == "2": menuType = "Appetizers"
    elif menuType_Option == "3": menuType = "Desserts"
    elif menuType_Option == "4": menuType = "Beverages"
    else:
        print("Invalid menu type. Please try again.")
        return

    # Write in Menu.txt
    try:
        with open('Menu.txt', 'a') as file:
            file.write(new_MenuItemID + "," +
                       newMenuName + ",RM " +
                       menuPrice + "," +
                       menuType + "\n")
    except FileNotFoundError:
        print("Can't read Rooms.txt, Please try again.")

    print("\nMenu " + new_MenuItemID + " added successfully.")


def MenuID_Generator(prefix):
    max_MenuNumber = 0
    try:
        with open('Menu.txt') as file:
            for line in file:
                MenuItem_Information = line.strip().split(",")
                MenuID               = MenuItem_Information[0]

                if MenuID.startswith(prefix):
                    current_MenuNumber = int(MenuID.split(prefix)[1])
                    if current_MenuNumber > max_MenuNumber:
                        max_MenuNumber = current_MenuNumber
    except FileNotFoundError:
            print("Can't read Booking.txt, Please try again.")

    return str(max_MenuNumber + 1)


def Update_Menu_Item():
    print("==================== Update Room Information =====================")
    MenuID_ToUpdate = input("Please enter menu ID to update: ").strip()

    if MenuID_ToUpdate == "":
        print("Menu ID cannot be empty. Please try again.")
        return

    updated_Lines  = []
    menuItem_Found = 0

    try:
        with open('Menu.txt') as file:
            for line in file:
                menu_Information = line.strip().split(",")
                MenuID           = menu_Information[0]
                MenuName         = menu_Information[1]
                MenuPrice        = menu_Information[2]
                MenuType         = menu_Information[3]

                if MenuID == MenuID_ToUpdate:
                    menuItem_Found += 1
                    while True:
                        print("")
                        print("Menu ID: "    + MenuID)
                        print("Menu Name: "  + MenuName)
                        print("Menu Price: " + MenuPrice)
                        print("Menu Type: "  + MenuType)
                        print("")
                        print("1. Menu Name")
                        print("2. Menu Price")
                        print("3. Menu Type")
                        print("0. Exit / Finish")
                        updateOption = input("Please select a room " + MenuID_ToUpdate + " information to update: ")

                        if updateOption   == "1": MenuName  = input("Please enter new menu item name: ")
                        elif updateOption == "2": MenuPrice = input("Please enter new menu item price: RM ")
                        elif updateOption == "3":
                            print("")
                            print("1. Mains")
                            print("2. Appetizers")
                            print("3. Desserts")
                            print("4. Beverages")
                            newMenuType_Option = input("Please enter new menu item type: ")

                            if newMenuType_Option   == "1": MenuName = "Mains"
                            elif newMenuType_Option == "2": MenuName = "Appetizers"
                            elif newMenuType_Option == "3": MenuName = "Desserts"
                            elif newMenuType_Option == "4": MenuName = "Beverages"
                            else: print("Invalid menu item type. Please try again.")

                        elif updateOption == "0": break
                        else: print("Invalid option. Please try again.")

                    updated_Lines.append(MenuID_ToUpdate + "," +
                                         MenuName + ",RM " +
                                         MenuPrice + "," +
                                         MenuType + "\n")
                else: updated_Lines.append(line)

    except FileNotFoundError:
        print("Can't read Menu.txt, Please try again.")
        return

    if menuItem_Found == 0:
        print("Menu " + MenuID_ToUpdate + " does not exist. Please try again.")
        return

    try:
        with open('Menu.txt', 'w') as file:
            file.writelines(updated_Lines)
        print("Room " + MenuID_ToUpdate + " updated successfully.")
    except FileNotFoundError:
        print("Can't read Menu.txt, Please try again.")



def main():
    while True:
        dashboard()
        role_Selected = input("Please Select your role: ")
        match role_Selected:
            # ============================================================================================================= #
            #                                              ADMINISTRATOR                                                    #
            # ============================================================================================================= #
            case "1":
                logged_in_user = credential_Validation("Administrator")
                if logged_in_user:
                    while True:
                        print("==================== Hotel Management System (Administrator) ====================")
                        print("WELCOME BACK, " + logged_in_user.userName)
                        print( "1. Add New Rooms")          # Add New Rooms: Add details of new rooms (Room number, type, price, availability).
                        print("2. Remove Rooms")            # Remove Rooms: Remove a room from the system by its room number.
                        print("3. Update Room Information") # Update Room Information: Edit room details (e.g., price, availability status).
                        print("4. Generate Reports")        # Generate Reports: Summarize total bookings and room availability.
                        print("5. View All Data")           # View All Data: Display all room and booking information for administrative review.
                        print("0. Back")                    # Back to Main Dashboard
                        print("")
                        administrator_Option = input("Please Select your option: ")

                        if   administrator_Option == "1": Add_New_Rooms()
                        elif administrator_Option == "2": Remove_Rooms()
                        elif administrator_Option == "3": Update_Room_Information()
                        elif administrator_Option == "4": print("4. Generate Reports")
                        elif administrator_Option == "5": View_All_Data()
                        elif administrator_Option == "0": break
                        else:                             print("Invalid Option. Please try again")  # Invalid input
            # ============================================================================================================= #
            #                                             RECEPTIONIST                                                      #
            # ============================================================================================================= #
            case "2":
                logged_in_user = credential_Validation("Receptionist")
                if logged_in_user:
                    while True:
                        print("==================== Hotel Management System (Receptionist) ====================")
                        print("WELCOME BACK, " + logged_in_user.userName)
                        print("1. Check Room Availability")     # Check Room Availability: View available rooms based on type (e.g., Single, Double, Suite).
                        print("2. View Booking Request")        # View Booking Request: View a room booking request (accept / reject)
                        print("3. View Cancel Booking Request") # Cancel Booking: Remove a booking and update room availability.
                        print("4. Update Guest Details")        # Update Guest Details: Edit guest information for an existing booking.
                        print("5. View All Bookings")           # View All Bookings: Display all current and past bookings.
                        print("0. Back")                        # Back to Main Dashboard
                        print("")
                        receptionist_Option = input("Please Select your option: ")

                        if receptionist_Option   == "1": Check_Room_Availability()
                        elif receptionist_Option == "2": View_Booking_Request()
                        elif receptionist_Option == "3": View_Cancel_Booking_Request()
                        elif receptionist_Option == "4": print("4. Update Guest Details")
                        elif receptionist_Option == "5": View_All_Booking()
                        elif receptionist_Option == "0": break
                        else:                            print("Invalid Option. Please try again") # Invalid Input
            # ============================================================================================================= #
            #                                            HOTEL GUEST                                                        #
            # ============================================================================================================= #
            case "3":
                logged_in_user = credential_Validation("Hotel Guest")
                if logged_in_user:
                    while True:
                        print("==================== Hotel Management System (Hotel Guest) ====================")
                        print("WELCOME BACK, " + logged_in_user.userName)
                        print("1. View Booking Details") # View Booking Details: Access booking details (room number, dates, price).
                        print("2. Booking Room")         # Book Room: Book a room booking with guest details (name, contact, room number, duration).
                        print("3. Cancel Booking")       # Cancel Booking: Request to cancel a booking.
                        print("4. View Menu")            # View Food Orders: Access the list of current food orders placed for the room.
                        print("5. Order Food")           # Order Food: Select items from the menu, specify quantity, and place an order.
                        print("0. Back")                 # Back to Main Dashboard
                        print("")
                        hotelGuest_Option = input("Please Select your option: ")

                        if hotelGuest_Option   == "1": View_Booking_Details(logged_in_user)
                        elif hotelGuest_Option == "2": Booking_Room(logged_in_user)
                        elif hotelGuest_Option == "3": Cancel_Booking(logged_in_user)
                        elif hotelGuest_Option == "4": View_Menu()
                        elif hotelGuest_Option == "5": Order_Food(logged_in_user)
                        elif hotelGuest_Option == "0": break
                        else:                          print("Invalid Option. Please try again") # Invalid Input
            # ============================================================================================================= #
            #                                           RESTAURANT MANAGER                                                  #
            # ============================================================================================================= #
            case "4":
                logged_in_user = credential_Validation("Restaurant Manager")
                if logged_in_user:
                    while True:
                        print("==================== Hotel Management System (Restaurant Manager) ====================")
                        print("WELCOME BACK, " + logged_in_user.userName)
                        print("1. Add New Menu Items")    # Add New Menu Items: Record new dishes to the menu (name, price, category).
                        print("2. Update Menu Items")     # Update Menu Items: Edit details of existing menu items (e.g., price or availability).
                        print("3. View Menu")             # View Menu: Display the current menu with all items and prices.
                        print("4. Record Food Orders")    # Record Food Orders: Record food orders from guests, including room number and items ordered.
                        print("5. Generate Sales Report") # Generate Sales Report: Summarize total sales and most popular dishes.
                        print("0. Back")                  # Back to Main Dashboard
                        print("")
                        restaurantManager_Option = input("Please Select your option: ")

                        if   restaurantManager_Option == "1": Add_Memu_Items()
                        elif restaurantManager_Option == "2": Update_Menu_Item()
                        elif restaurantManager_Option == "3": View_Menu()
                        elif restaurantManager_Option == "4": print("4. Record Food Orders")
                        elif restaurantManager_Option == "5": print("5. Generate Sales Report")
                        elif restaurantManager_Option == "0": break
                        else:                                 print("Invalid Option. Please try again")
            case "0":
                print("==================== Hotel Management System ====================")
                choice = input("Are you sure you want to exit? (Y/N): ")
                if   choice.capitalize() == "Y": break
                elif choice.capitalize() == "N": print("Continuing...")
                else:                            print("Invalid Input. Please try again.")
            case _: print("Invalid Role. Please try again.")

main()