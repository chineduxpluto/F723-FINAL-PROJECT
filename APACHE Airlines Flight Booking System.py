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