'''
CST8002 - Programming Language Research Project
Professor: Tyler DeLay
Author: Aly Kaamoush
Date: March 16, 2025
Description: Presentation layer for console user interface with support for polymorphic record display
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
        print("7. Change display format")
        print("8. Visualize data")
        print("9. Exit")
        print("\nEnter your choice (1-9): ")

    def display_records(self, records, start_index=0):
        '''Display one or multiple records using polymorphic format_for_display method'''
        if not records:
            print("\nNo records to display")
            return
            
        for i, record in enumerate(records):
            print("\n" + "=" * 50)
            print(f"{self.author_name}")
            print("=" * 50)
            print(f"\nRecord #{start_index + i + 1}")
            # Use polymorphic method instead of individual field display
            print(record.format_for_display())

    def get_record_input(self):
        '''Get user input for record fields'''
        record = DwellingRecord()  # Use base class for user input
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

    def change_display_format(self):
        '''Allow user to change the display format'''
        print("\nChoose display format:")
        print("1. Standard (Default)")
        print("2. Detailed")
        print("3. Summary")
        
        choice = input("Enter choice (1-3): ").strip()
        
        if choice == "1":
            self.manager.set_display_mode("standard")
            print("\nDisplay format set to Standard")
        elif choice == "2":
            self.manager.set_display_mode("detailed")
            print("\nDisplay format set to Detailed")
        elif choice == "3":
            self.manager.set_display_mode("summary")
            print("\nDisplay format set to Summary")
        else:
            print("\nInvalid choice. Format unchanged.")

    def display_visualization_menu(self):
        '''Display the visualization menu'''

        print("\n" + "=" * 50)
        print(self.author_name)
        print("=" * 50)
        print("\nVisualization Options")
        print("1. Vertical Bar Chart")
        print("2. Horizontal Bar Chart")
        print("3. Return to Main Menu")
        print("\nEnter your choice (1-3): ")

    def handle_visualization(self):
        '''Handle visualization functionality'''
        from presentation.visualization import ChartGenerator
        
        # Check if we have data to visualize
        if not self.manager.records:
            print("\nNo data available for visualization. Please load data first.")
            return
            
        while True:
            self.display_visualization_menu()
            choice = input().strip()
            
            print(f"\n{self.author_name}")
            
            if choice == '1' or choice == '2':
                # Get field to visualize
                fields = self.manager.get_visualization_options()
                print("\nSelect field to visualize:")
                for i, field in enumerate(fields):
                    display_name = self.manager.get_field_display_name(field)
                    print(f"{i+1}. {display_name}")
                
                try:
                    field_choice = int(input(f"Enter choice (1-{len(fields)}): ")) - 1
                    if field_choice < 0 or field_choice >= len(fields):
                        print("\nInvalid choice")
                        continue
                        
                    selected_field = fields[field_choice]
                    display_name = self.manager.get_field_display_name(selected_field)
                    
                    # Get data for visualization
                    labels, values = self.manager.get_data_for_visualization(selected_field)
                    
                    if not labels or not values:
                        print(f"\nNo data available for visualization with {display_name}. The field may be empty in your dataset.")
                        continue
                    
                    # Create chart
                    chart_generator = ChartGenerator()
                    
                    # Customize title and labels based on the field
                    if selected_field == 'original_value':
                        title = "Average Values by Year"
                        x_label = "Year"
                        y_label = "Average Value"
                    elif selected_field == 'period':
                        title = "Number of Records by Year"
                        x_label = "Year"
                        y_label = "Number of Records"
                    else:
                        title = f"Average Values by {display_name}"
                        x_label = display_name
                        y_label = "Average Value"
                    
                    if choice == '1':
                        # Vertical bar chart
                        chart_generator.create_vertical_bar_chart(
                            labels, values, title, x_label, y_label)
                    else:
                        # Horizontal bar chart
                        chart_generator.create_horizontal_bar_chart(
                            labels, values, title, y_label, x_label)
                    
                except ValueError:
                    print("\nInvalid input. Please enter a number.")
                
            elif choice == '3':
                break
            
            else:
                print("\nInvalid choice. Please try again.")

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
                self.change_display_format()
                    
            elif choice == '8':
                self.handle_visualization()
            
            elif choice == '9':
                print("\nThank you for using the system!")
                break
            
            else:
                print("\nInvalid choice. Please try again.")

    