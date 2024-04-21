import random
import string

class SeatBookingSystem:
    def __init__(self):
        """
            Initialize the seat booking system with a seat layout for a fictional aircraft.
            The seats are organized into a dictionary with keys as seat identifiers (e.g., '1A', '1B', ...)
            and values as the seat status ('F' for free, 'X' for aisle, 'S' for storage, 'R' for reserved).
        """
        self.seats = {}
        self.bookings = {}
        rows = range(1, 81)  # Rows from 1 to 80
        columns = ['A', 'B', 'C', 'D', 'E', 'F'] # Columns labeled from A to F.
        # Example fill in based on a simple pattern
        for row in rows:
            for col in columns:
                seat_id = f"{row}{col}"
                if col in ['B', 'E']:  # Assume isles are at columns B and E arbitrarily
                    self.seats[seat_id] = 'X'
                elif col in ['C', 'D'] and row % 10 == 0:  # # Place storage areas at every 10th row in columns C and D.
                    self.seats[seat_id] = 'S'
                else:
                    self.seats[seat_id] = 'F'

    def generate_unique_booking_reference(self):
        """Generate a unique booking reference that has not been produced before."""
        while True:
            # Generate a random 8-character alphanumeric string
            reference = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
            # Check if this reference has already been used
            if reference not in self.bookings:
                return reference # Return the reference only if it's not it's not already in use

    def check_seat_availability(self, seat_id):
        """
        Check the availability of a specified seat.

        Parameters:
        seat_id (str): The identifier for the seat (e.g., '1A').

        Returns:
        str: A message indicating whether the seat is free, booked, not available, or invalid.
        """
        if seat_id in self.seats:
            status = self.seats[seat_id]
            if status == 'F':
                return f"Seat {seat_id} is free."
            elif status == 'R':
                # Retrieve the booking reference for the occupied seat to provide detailed feedback
                reference = next(ref for ref, seat in self.bookings.items() if seat == seat_id)
                return f"Seat {seat_id} is already booked (Reference: {reference})."
            elif status in ['X', 'S']:
                return f"Seat {seat_id} is not available for booking (Marked as {'aisle' if status == 'X' else 'storage'})."
        return "Invalid seat ID."

    def book_seat(self, seat_id):
        """
        Book a seat if it is available with a unique booking reference

        Parameters:
        seat_id (str): The identifier for the seat to book.

        Returns:
        str: A message indicating success if the seat is booked or why the booking failed.
        """
        if seat_id in self.seats and self.seats[seat_id] == 'F':
            reference = self.generate_unique_booking_reference()
            self.seats[seat_id] = 'R'  # Mark the seat as reserved
            self.bookings[reference] = seat_id  # Map the booking reference to the seat ID
            return f"Seat {seat_id} has been successfully booked with reference {reference}."
        elif seat_id in self.seats:
            return f"Seat {seat_id} cannot be booked."
        else:
            return "Invalid seat ID."

    def free_seat(self, seat_id):
        """
        Free a booked seat, making it available again for booking.

        Parameters:
        seat_id (str): The identifier for the seat to free.

        Returns:
        str: A message indicating whether the seat was freed or the reason it couldn't be freed.
        """
        if seat_id in self.seats and self.seats[seat_id] == 'R':
            # Find the booking reference associated with this seat
            reference = next(ref for ref, seat in self.bookings.items() if seat == seat_id)
            self.seats[seat_id] = 'F'  # Mark the seat as free
            del self.bookings[reference]  # Remove the booking reference
            return f"Seat {seat_id} has been freed, and booking reference {reference} removed."
        elif seat_id in self.seats:
            return f"Seat {seat_id} is not currently booked."
        else:
            return "Invalid seat ID."

    def show_booking_state(self):
        """
        Display the current booking state of all seats.

        Returns:
        str: A formatted string showing all seats and their current booking status.
        """
        result = []
        for seat_id, status in self.seats.items():
            if status == 'R':
                reference = next(ref for ref, seat in self.bookings.items() if seat == seat_id)
                result.append(f"{seat_id}: Booked (Reference {reference})")
            else:
                result.append(f"{seat_id}: {'Free' if status == 'F' else 'Unavailable'}")
        return "\n".join(result)

    def run(self):
        """
        Run the command line interface for the seat booking system. Presents a menu and handles user interactions.
        """
        menu = """
        1. Check seat availability
        2. Book a seat
        3. Free a seat
        4. Show booking state
        5. Exit
        """
        while True:
            print(menu)
            choice = input("Choose an option: ")
            if choice == '1':
                seat_id = input("Enter seat ID to check availability (e.g., 1A): ")
                print(self.check_seat_availability(seat_id))
            elif choice == '2':
                seat_id = input("Enter seat ID to book (e.g., 1A): ")
                print(self.book_seat(seat_id))
            elif choice == '3':
                seat_id = input("Enter seat ID to free (e.g., 1A): ")
                print(self.free_seat(seat_id))
            elif choice == '4':
                print(self.show_booking_state())
            elif choice == '5':
                print("Exiting the program.")
                break
            else:
                print("Invalid option, please try again.")

if __name__ == "__main__":
    system = SeatBookingSystem()
    system.run()
