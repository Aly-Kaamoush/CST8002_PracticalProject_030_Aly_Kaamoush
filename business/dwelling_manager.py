'''
CST8002 - Programming Language Research Project
Professor: Tyler DeLay
Author: Aly Kaamoush
Date: February 16, 2025
Description: Business layer for managing dwelling records operations
'''
from persistence.data_handler import DataHandler
from model.dwelling_record import DwellingRecord

class DwellingManager:
    '''Handles the business logic for managing dwelling records'''

    def __init__(self):
        '''Set up the manager with data handler and empty records list'''
        self.data_handler = DataHandler()
        self.records = []

    def load_records(self):
        '''Load or reload records from file'''
        self.records = self.data_handler.load_data()
        if len(self.records) > 0:
            return True
        return False
    
    def save_records(self):
        '''Save current records to a new file'''
        return self.data_handler.save_data(self.records)
    
    def display_one_record(self, index):
        '''Get a single record to display'''
        if index >= 0 and index < len(self.records):
            return self.records[index]
        return None
    
    def display_all_records(self):
        '''Get all records to display'''
        return self.records
    
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