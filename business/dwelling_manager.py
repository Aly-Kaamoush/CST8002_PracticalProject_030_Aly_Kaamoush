'''
CST8002 - Programming Language Research Project
Professor: Tyler DeLay
Author: Aly Kaamoush
Date: March 16, 2025
Description: Business layer for managing dwelling records operations with polymorphism support
'''
from persistence.data_handler import DataHandler
from model.dwelling_record import DwellingRecord, DetailedDwellingRecord, SummaryDwellingRecord

class DwellingManager:
    '''Handles the business logic for managing dwelling records'''

    def __init__(self):
        '''Set up the manager with data handler and empty records list'''
        self.data_handler = DataHandler()
        self.records = []
        self.display_mode = "standard"  # Options: "standard", "detailed", "summary"

    def load_records(self):
        '''Load or reload records from file'''
        self.records = self.data_handler.load_data()
        if len(self.records) > 0:
            return True
        return False
    
    def save_records(self):
        '''Save current records to a new file'''
        return self.data_handler.save_data(self.records)
    
    def set_display_mode(self, mode):
        '''Set the display mode for records
        Args:
            mode: String indicating display mode ("standard", "detailed", "summary")
        Returns:
            bool: True if mode was set successfully
        '''
        if mode in ["standard", "detailed", "summary"]:
            self.display_mode = mode
            return True
        return False
    
    def convert_record_to_display_type(self, record):
        '''Convert a record to appropriate display type based on current mode
        Args:
            record: A DwellingRecord object
        Returns:
            DwellingRecord or subclass: The appropriate record type based on display mode
        '''
        if not isinstance(record, DwellingRecord):
            return None
            
        if self.display_mode == "standard":
            return record
        
        # Create the appropriate specialized record type
        if self.display_mode == "detailed":
            display_record = DetailedDwellingRecord()
        else:  # summary mode
            display_record = SummaryDwellingRecord()
            
        # Copy data from original record
        display_record.set_csduid(record.get_csduid())
        display_record.set_csd(record.get_csd())
        display_record.set_period(record.get_period())
        display_record.set_indicator(record.get_indicator())
        display_record.set_unit_measure(record.get_unit_measure())
        display_record.set_original_value(record.get_original_value())
        
        return display_record
    
    def display_one_record(self, index):
        '''Get a single record to display with current format mode'''
        if index >= 0 and index < len(self.records):
            record = self.records[index]
            return self.convert_record_to_display_type(record)
        return None
    
    def display_multiple_records(self, start_index, count):
        '''
        Get multiple records to display with current format mode
        Args:
            start_index: Starting position in the list
            count: Number of records to display
        Returns:
            list: Requested records within valid range converted to display type
        '''
        if start_index < 0:
            start_index = 0
        end_index = min(start_index + count, len(self.records))
        
        # Convert each record to the appropriate display type
        display_records = []
        for i in range(start_index, end_index):
            display_records.append(self.convert_record_to_display_type(self.records[i]))
            
        return display_records
    
    def add_new_record(self, new_record):
        '''Add a new record to the list'''
        if isinstance(new_record, DwellingRecord):
            self.records.append(new_record)
            return True
        return False
    
    def edit_record(self, index, updated_record):
        '''Edit an existing record'''
        if index >= 0 and index < len(self.records):
            if isinstance(updated_record, DwellingRecord):
                self.records[index] = updated_record
                return True
        return False
    
    def delete_record(self, index):
        '''Delete a record from the list'''
        if index >= 0 and index < len(self.records):
            self.records.pop(index)
            return True
        return False