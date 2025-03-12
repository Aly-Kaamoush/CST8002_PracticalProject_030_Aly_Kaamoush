'''
CST8002 - Programming Language Research Project
Professor:  Tyler DeLay
Author: Aly Kaamoush
Date: March 16, 2025
Description: This file contains the base DwellingRecord class and its specialized subclasses
'''

# Part of Model Layer: This class represents the data structure for dwelling records

class DwellingRecord:
    '''A base class to represent a single dwelling unit record from the dataset.
    Uses column names from the CSV file as variable names.
    '''
    def __init__(self):
        ''' Initializing an empty dwelling constructor with default values.'''
        self._csduid = 0
        self._csd = ""
        self._period = 0
        self._indicator = ""
        self._unit_measure = 0.0
        self._original_value = 0.0

    def get_csduid(self):
        '''Return the CSDUID value.'''
        return self._csduid

    def set_csduid(self, value):
        '''Set the CSDUID value.'''
        self._csduid = value

    def get_csd(self):
        '''Return the CSD name.'''
        return self._csd

    def set_csd(self, value):
        '''Set the CSD name.'''
        self._csd = value

    def get_period(self):
        '''Return the period value.'''
        return self._period

    def set_period(self, value):
        '''Set the period value.'''
        self._period = value

    def get_indicator(self):
        '''Return the indicator summary description.'''
        return self._indicator

    def set_indicator(self, value):
        '''Set the indicator summary description.'''
        self._indicator = value

    def get_unit_measure(self):
        '''Return the unit of measure value.'''
        return self._unit_measure

    def set_unit_measure(self, value):
        '''Set the unit of measure value.'''
        self._unit_measure = value

    def get_original_value(self):
        '''Return the original value.'''
        return self._original_value

    def set_original_value(self, value):
        '''Set the original value.'''
        self._original_value = value

    def format_for_display(self):
        '''Base method to format record for display - will be overridden in subclasses.
        Returns a formatted string representation of the record.
        '''
        return (f"CSDUID: {self._csduid}\n"
                f"CSD: {self._csd}\n"
                f"Period: {self._period}\n"
                f"Indicator Summary Description: {self._indicator}\n"
                f"Unit of Measure: {self._unit_measure}\n"
                f"Original Value: {self._original_value}")
    
class DetailedDwellingRecord(DwellingRecord):
    '''A specialized class (Sub-Class) for displaying dwelling records with detailed formatting.
    Includes additional analysis like percent change or growth indicators.
    '''
    def __init__(self):
        '''Initialize with parent constructor'''
        super().__init__()
    
    def format_for_display(self):
        '''Override base method to provide detailed formatted view with additional analysis.
        Returns an enhanced string representation with growth indicators.
        '''
        # Calculate growth indicator based on value
        growth_indicator = "▲ Growing" if self._original_value > 50 else "▼ Declining"
        
        # Format with enhanced details and visual indicators
        return (f"DETAILED RECORD VIEW\n"
                f"==========================================\n"
                f"Location ID: {self._csduid} - {self._csd}\n"
                f"Time Period: {self._period}\n"
                f"Measurement: {self._indicator}\n"
                f"Value: {self._original_value:,.2f} {self._unit_measure}\n"
                f"Status: {growth_indicator}\n"
                f"==========================================")


class SummaryDwellingRecord(DwellingRecord):
    '''A specialized class (Sub-Class) for displaying dwelling records in a concise summary format.
    Shows only essential information.
    '''
    def __init__(self):
        '''Initialize with parent constructor'''
        super().__init__()
    
    def format_for_display(self):
        '''Override base method to provide a concise summary view.
        Returns a minimal string representation with core data.
        '''
        return (f"SUMMARY: {self._csd} ({self._period}) - {self._indicator}: "
                f"{self._original_value:,.2f} {self._unit_measure}")


