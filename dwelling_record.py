'''
CST8002 - Python Programming
Professor:  Tyler DeLay
Author: Aly Kaamoush
Date: January 26, 2025
Description: This file contains the DwellingRecord class for storing and managing dwelling unit data
'''

class DwellingRecord:
    ''' A class to recrd a single dwelling unit record from the dataset. '''
    def __init_(self):
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


