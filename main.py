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

Example Program Outline
Here’s a general structure to get started with the project:
- Main Menu: Display options for selecting a role (e.g., Administrator, Receptionist).
- Role-Specific Menus: Based on the role selected, show relevant functionalities.
- File Operations: Read, write, update, and delete data in respective files for each functionality.
- Error Handling: Include checks to handle file access errors and validate user input.
"""