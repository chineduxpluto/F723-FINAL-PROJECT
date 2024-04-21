class SeatBookingSystem:
    def __init(self):
        # Initializing the seat layout on a larger scale from 1A to 80F, with appropriate 'X' and 'S' markings
        self.seats = {}
        rows = range(1, 81)  # Rows from 1 to 80
        columns = ['A', 'B', 'C', 'D', 'E', 'F']
        # Example fill in based on a simple pattern
        for row in rows:
            for col in columns:
                seat_id = f"{row}{col}"
                if col in ['B', 'E']:  # Assume isles are at columns B and E arbitrarily
                    self.seats[seat_id] = 'X'
                elif col in ['C', 'D'] and row % 10 == 0:  # Storage every 10th row in columns C and D
                    self.seats[seat_id] = 'S'
                else:
                    self.seats[seat_id] = 'F'