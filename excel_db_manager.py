import pandas as pd

class ExcelDatabaseManager:
    def __init__(self, filename):
        """
        Initialize the Excel database manager with the specified Excel filename.
        This method calls load_or_create_sheet to prepare the data file.

        Args:
        filename (str): The path to the Excel file used for storing booking data.
                """
        self.filename = filename
        self.load_or_create_sheet()

    def load_or_create_sheet(self):
        """
        Load the existing Excel file or create a new one if it doesn't exist.
        This method tries to read an Excel file and creates one with necessary columns
        if the file is not found.
        """
        try:
            # Attempt to load an existing Excel file
            self.df = pd.read_excel(self.filename, engine='openpyxl')
        except FileNotFoundError:
            # Define columns for a new Excel file and create it
            self.df = pd.DataFrame(columns=['Reference', 'Passport Number', 'First Name', 'Last Name', 'Seat ID'])
            self.df.to_excel(self.filename, index=False, engine='openpyxl')

    def add_booking(self, reference, passport_number, first_name, last_name, seat_id):
        """
        Add a new booking to the Excel spreadsheet.

        Args:
        reference (str): Unique booking reference identifier.
        passport_number (str): Passport number of the traveler.
        first_name (str): First name of the traveler.
        last_name (str): Last name of the traveler.
        seat_id (str): The seat ID corresponding to the booking.

        This method appends a new row to the DataFrame and saves the file.
        """
        new_row = pd.DataFrame([{
            'Reference': reference,
            'Passport Number': passport_number,
            'First Name': first_name,
            'Last Name': last_name,
            'Seat ID': seat_id
        }])
        self.df = pd.concat([self.df, new_row], ignore_index=True)
        self.df.to_excel(self.filename, index=False, engine='openpyxl')

    def remove_booking(self, reference):
        """
        Remove a booking from the Excel spreadsheet based on the booking reference.

        Args:
        reference (str): The booking reference of the booking to remove.

        This method filters out the row with the given reference and saves the file.
        """
        self.df = self.df[self.df['Reference'] != reference]
        self.df.to_excel(self.filename, index=False, engine='openpyxl')

    def save_changes(self):
        """
        Explicitly save changes to the Excel file to ensure data persistence.

        This method is useful for confirming all changes are written to the disk.
        """
        try:
            self.df.to_excel(self.filename, index=False, engine='openpyxl')
            print("Data successfully saved to Excel.")
        except Exception as e:
            print("Failed to save data to Excel:", e)

    def close(self):
        """Close any resources if necessary. Currently, just ensure the DataFrame is saved."""
        self.save_changes()  # Make sure all changes are written back to the Excel file
