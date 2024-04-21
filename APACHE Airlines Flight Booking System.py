class SeatBookingSystem:
    def __init(self):
        """
            Initialize the seat booking system with a seat layout for a fictional aircraft.
            The seats are organized into a dictionary with keys as seat identifiers (e.g., '1A', '1B', ...)
            and values as the seat status ('F' for free, 'X' for aisle, 'S' for storage, 'R' for reserved).
        """
        self.seats = {}
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

    def check_seat_availability(self, seat_id):
        """
        Check the availability of a specified seat.

        Parameters:
        seat_id (str): The identifier for the seat (e.g., '1A').

        Returns:
        str: A message indicating whether the seat is free, booked, not available, or invalid.
        """
        if seat_id in self.seats:
            if self.seats[seat_id] == 'F':
                return f"Seat {seat_id} is free."
            elif self.seats[seat_id] == 'R':
                return f"Seat {seat_id} is already booked."
            else:
                return f"Seat {seat_id} is not available for booking (isle or storage)."
        return "Invalid seat ID."

    def book_seat(self, seat_id):
        """
        Book a seat if it is available.

        Parameters:
        seat_id (str): The identifier for the seat to book.

        Returns:
        str: A message indicating success if the seat is booked or why the booking failed.
        """
        if seat_id in self.seats:
            if self.seats[seat_id] == 'F':
                self.seats[seat_id] = 'R'
                return f"Seat {seat_id} has been successfully booked."
            elif self.seats[seat_id] in ['R', 'X', 'S']:
                return f"Seat {seat_id} cannot be booked."
        return "Invalid seat ID."

    def free_seat(self, seat_id):
        """
        Free a booked seat, making it available again for booking.

        Parameters:
        seat_id (str): The identifier for the seat to free.

        Returns:
        str: A message indicating whether the seat was freed or the reason it couldn't be freed.
        """
        if seat_id in self.seats:
            if self.seats[seat_id] == 'R':
                self.seats[seat_id] = 'F'
                return f"Seat {seat_id} has been freed."
            else:
                return f"Seat {seat_id} is not currently booked or not bookable."
        return "Invalid seat ID."

    def show_booking_state(self):
        """
        Display the current booking state of all seats.

        Returns:
        str: A formatted string showing all seats and their current booking status.
        """
        result = []
        for seat_id, status in self.seats.items():
            result.append(f"{seat_id}: {'Booked' if status == 'R' else 'Free' if status == 'F' else 'Unavailable'}")
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
