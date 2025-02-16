'''
CST8002 - Programming Language Research Project
Professor: Tyler DeLay
Author: Aly Kaamoush
Date: February 16, 2025
Description: Presentation layer for console user interface
'''

from business.dwelling_manager import DwellingManager
from model.dwelling_record import DwellingRecord

class ConsoleUI:
    '''Handles user interface and interaction'''

    def __init__(self):
        '''Intialize the console UI'''
        self.manager = DwellingManager()
        self.author_name = "Program by Aly Kaamoush"

    def display_menu(self):
        '''Display the main menu'''
        print("\n" + "=" * 50)
        print(self.author_name)
        print("=" * 50)
        print("\nDwelling Records Management System")
        print("1. Reload data from file")
        print("2. Save data to new file")
        print("3. Display records")
        print("4. Add new record")
        print("5. Edit record")
        print("6. Delete record")
        print("7. Exit")
        print("\nEnter your choice (1-7): ")

    def display_records(self, records, start_index=0):
        '''Display one or multiple records'''
        if not records:
            print("\nNo records to display")
            return
            
        for i, record in enumerate(records):
            print("\n" + "=" * 50)
            print(f"{self.author_name}")
            print("=" * 50)
            print(f"\nRecord #{start_index + i+ 1}")
            print(f"CSDUID: {record.get_csduid()}")
            print(f"CSD: {record.get_csd()}")
            print(f"Period: {record.get_period()}")
            print(f"Indicator Summary Description: {record.get_indicator()}")
            print(f"Unit of Measure: {record.get_unit_measure()}")
            print(f"Original Value: {record.get_original_value()}")

    def get_record_input(self):
        '''Get user input for record fields'''
        record = DwellingRecord()
        try:
            record.set_csduid(int(input("Enter CSDUID: ")))
            record.set_csd(input("Enter CSD: "))
            record.set_period(int(input("Enter Period: ")))
            record.set_indicator(input("Enter Indicator Summary Description: "))
            record.set_unit_measure(float(input("Enter Unit of Measure: ")))
            record.set_original_value(float(input("Enter Original Value: ")))
            return record
        except ValueError:
            print("\nInvalid input. Please enter correct data types.")
            return None

    def run(self):
        '''Main application loop'''
        # Load initial data
        if not self.manager.load_records():
            print("\nWarning: Initial data load failed")
            
        while True:
            self.display_menu()
            choice = input().strip()
            
            print(f"\n{self.author_name}")
            
            if choice == '1':
                if self.manager.load_records():
                    print("\nData reloaded successfully")
                else:
                    print("\nFailed to reload data")

            elif choice == '2':
                filename = self.manager.save_records()
                if filename:
                    print(f"\nData saved to {filename}")
                else:
                    print("\nFailed to save data")

            elif choice == '3':
                print("\nDisplay options:")
                print("1. Display one record")
                print("2. Display multiple records")
                display_choice = input("Enter choice (1-2): ")
                
                if display_choice == '1':
                    try:
                        index = int(input("Enter record number: ")) - 1
                        record = self.manager.display_one_record(index)
                        if record:
                            self.display_records([record], start_index=index)
                        else:
                            print("\nRecord not found")
                    except ValueError:
                        print("\nInvalid input")
                elif display_choice == '2':
                    try:
                        start = int(input("Enter starting record number: ")) - 1
                        count = int(input("Enter number of records to display: "))
                        records = self.manager.display_multiple_records(start, count)
                        self.display_records(records, start_index=start)
                    except ValueError:
                        print("\nInvalid input")

            elif choice == '4':
                record = self.get_record_input()
                if record and self.manager.add_new_record(record):
                    print("\nRecord added successfully")
                else:
                    print("\nFailed to add record")

            elif choice == '5':
                try:
                    index = int(input("Enter record number to edit: ")) - 1
                    record = self.get_record_input()
                    if record and self.manager.edit_record(index, record):
                        print("\nRecord updated successfully")
                    else:
                        print("\nFailed to update record")
                except ValueError:
                    print("\nInvalid input")

            elif choice == '6':
                try:
                    index = int(input("Enter record number to delete: ")) - 1
                    if self.manager.delete_record(index):
                        print("\nRecord deleted successfully")
                    else:
                        print("\nFailed to delete record")
                except ValueError:
                    print("\nInvalid input")
                    
            elif choice == '7':
                print("\nThank you for using the system!")
                break
            
            else:
                print("\nInvalid choice. Please try again.")

    