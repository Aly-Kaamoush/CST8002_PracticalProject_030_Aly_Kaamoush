'''
CST8002 - Programming Language Research Project
Professor: Tyler DeLay
Author: Aly Kaamoush
Date: February 16, 2025
Description: Presentation layer for console user interface
'''

from business.dwelling_manager import DwellingManager

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
        print("4. Exit")
        print("\nEnter your choice (1-4): ")

    def display_records(self, records):
        '''Display one or multiple records'''
        if not records:
            print("\nNo records to display")
            return
            
        for i, record in enumerate(records):
            print("\n" + "=" * 50)
            print(f"{self.author_name}")
            print("=" * 50)
            print(f"\nRecord #{i + 1}")
            print(f"CSDUID: {record.get_csduid()}")
            print(f"CSD: {record.get_csd()}")
            print(f"Period: {record.get_period()}")
            print(f"Indicator: {record.get_indicator()}")
            print(f"Unit of Measure: {record.get_unit_measure()}")
            print(f"Original Value: {record.get_original_value()}")

    def run(self):
        '''Main application loop'''
        # Load initial data
        if not self.manager.load_records():
            print("Warning: Initial data load failed")
            
        while True:
            self.display_menu()
            choice = input().strip()
            
            print(f"\n{self.author_name}")
            
            if choice == '1':
                if self.manager.load_records():
                    print("Data reloaded successfully")
                else:
                    print("Failed to reload data")

            elif choice == '2':
                filename = self.manager.save_records()
                if filename:
                    print(f"Data saved to {filename}")
                else:
                    print("Failed to save data")

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
                            self.display_records([record])
                        else:
                            print("Record not found")
                    except ValueError:
                        print("Invalid input")
                elif display_choice == '2':
                    try:
                        start = int(input("Enter starting record number: ")) - 1
                        count = int(input("Enter number of records to display: "))
                        records = self.manager.display_multiple_records(start, count)
                        self.display_records(records)
                    except ValueError:
                        print("Invalid input")
                    
            elif choice == '4':
                print("Thank you for using the system!")
                break
            
            else:
                print("Invalid choice. Please try again.")

    