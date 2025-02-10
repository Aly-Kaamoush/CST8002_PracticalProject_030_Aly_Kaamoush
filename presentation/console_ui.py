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
        print("3. Exit")
        print("\nEnter your choice (1-3): ")

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
                print("Thank you for using the system!")
                break
            
            else:
                print("Invalid choice. Please try again.")

    