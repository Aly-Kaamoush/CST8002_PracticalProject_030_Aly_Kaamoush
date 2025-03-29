'''
CST8002 - Programming Language Research Project
Professor: Tyler DeLay
Author: Aly Kaamoush
Date: April 6, 2025
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
    
    def get_data_for_visualization(self, field_name):
        '''
        Process data for visualization based on a selected field
        
        Args:
            field_name: Name of the field to visualize (e.g., 'period', 'csduid')
        
        Returns:
            tuple: (labels, values) for chart generation
        '''
        if not self.records:
            return [], []
        
        # Special case for visualizing original_value directly
        if field_name == 'original_value':
            # For original value, we should group by something meaningful
            # Let's try grouping by period (year) or by CSD (location)
            group_by_field = 'period'  # You could also use 'csd' here
            
            field_values = {}
            for record in self.records:
                # Get the grouping key
                if group_by_field == 'period':
                    key = record.get_period()
                else:  # group by csd
                    key = record.get_csd()
                    
                if key is not None and key != '' and key != 0:
                    if key not in field_values:
                        field_values[key] = []
                    value = record.get_original_value()
                    if value is not None:
                        field_values[key].append(value)
            
            # Sort keys (convert to strings for comparison if needed)
            sorted_keys = sorted(field_values.keys())
            
            labels = []
            values = []
            for key in sorted_keys:
                if field_values[key]:  # Only include if there are values
                    labels.append(str(key))
                    values.append(sum(field_values[key]) / len(field_values[key]))
            
            return labels, values
        
        # For other fields - group records by the selected field
        field_getters = {
            'csduid': lambda record: record.get_csduid(),
            'csd': lambda record: record.get_csd(),
            'period': lambda record: record.get_period(),
            'indicator': lambda record: record.get_indicator(),
            'unit_measure': lambda record: record.get_unit_measure()
        }
        
        if field_name not in field_getters:
            return [], []
        
        # Group records by the selected field
        field_values = {}
        for record in self.records:
            key = field_getters[field_name](record)
            # Skip empty or None keys
            if key is None or key == '' or key == 0:
                continue
                
            if key not in field_values:
                field_values[key] = []
                
            value = record.get_original_value()
            if value is not None:
                field_values[key].append(value)
        
        # Calculate average for each group
        labels = []
        values = []
        for key in sorted(field_values.keys()):
            if field_values[key]:  # Only include if there are values
                labels.append(str(key))
                values.append(sum(field_values[key]) / len(field_values[key]))
        
        return labels, values

    def get_visualization_options(self):
        '''
        Get available fields for visualization
        
        Returns:
            list: Names of fields available for visualization
        '''
        return ['csduid', 'csd', 'period', 'indicator', 'unit_measure', 'original_value']

    def get_field_display_name(self, field_name):
        '''
        Get a display-friendly name for a field
        
        Args:
            field_name: Technical field name
        
        Returns:
            str: Display-friendly field name
        '''
        display_names = {
            'csduid': 'Census Subdivision ID (csduid)',
            'csd': 'Census Subdivision (csd)',
            'period': 'Time Period (period)',
            'indicator': 'IndicatorSummaryDescription',
            'unit_measure': 'Unit of Measure',
            'original_value': 'Original Value'
        }
        
        return display_names.get(field_name, field_name)