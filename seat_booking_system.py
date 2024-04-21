# seat_booking_system.py
from excel_db_manager import ExcelDatabaseManager
import random
import string

class SeatBookingSystem:
    def __init__(self):
        """
        Initialize the seat booking system. This sets up the connection to the Excel database
        to manage booking data and initializes the seating map for the aircraft.
        """
        self.db_manager = ExcelDatabaseManager('bookings.xlsx')
        self.seats = {f"{row}{col}": 'F' for row in range(1, 81) for col in 'ABCDEF'}

    def generate_unique_booking_reference(self):
        """
        Generate a unique booking reference. Ensures that no two bookings have the same reference.

        Returns:
        str: A unique booking reference consisting of 8 alphanumeric characters.
        """
        existing_refs = set(self.db_manager.df['Reference'])
        while True:
            reference = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
            if reference not in existing_refs:
                return reference

    def book_seat(self, seat_id, passport_number, first_name, last_name):
        """
        Book a seat if it is available. Adds booking details to the Excel database.

        Args:
        seat_id (str): The ID of the seat to book.
        passport_number (str): Passport number of the passenger.
        first_name (str): First name of the passenger.
        last_name (str): Last name of the passenger.

        Returns:
        str: Confirmation message indicating whether the booking was successful or not.
        """
        if self.seats.get(seat_id, '') == 'F':
            reference = self.generate_unique_booking_reference()
            print(f"Booking seat: {seat_id}")
            self.db_manager.add_booking(reference, passport_number, first_name, last_name, seat_id)
            self.seats[seat_id] = 'R'
            print(f"Seat {seat_id} booked with reference {reference}.")
            return f"Seat {seat_id} booked with reference {reference}."
        return "Seat not available or invalid."

    def free_seat(self, seat_id):
        """
        Free a seat and remove the associated booking from the Excel database.

        Args:
        seat_id (str): The ID of the seat to free.

        Returns:
        str: Confirmation message indicating whether the seat was successfully freed or not.
        """
        for index, row in self.db_manager.df.iterrows():
            if row['Seat ID'] == seat_id:
                reference = row['Reference']
                self.db_manager.remove_booking(reference)
                self.seats[seat_id] = 'F'
                return f"Booking reference {reference} has been canceled and seat {seat_id} freed."
        return "No active booking found for this seat."

    def check_seat_availability(self, seat_id):
        """
        Check the availability of a specified seat.

        Args:
        seat_id (str): The ID of the seat to check.

        Returns:
        str: Message indicating if the seat is free or already booked.
        """
        if self.seats.get(seat_id, '') == 'F':
            return f"Seat {seat_id} is free."
        elif self.seats.get(seat_id, '') == 'R':
            return f"Seat {seat_id} is already booked."
        return "Invalid seat ID."



if __name__ == "__main__":
    manager = ExcelDatabaseManager("bookings.xlsx")
    manager.add_booking("TEST1234", "1234567890", "Jane", "Doe", "1B")
    # manager.remove_booking("TEST1234")
    manager.save_changes()
    manager.close()

