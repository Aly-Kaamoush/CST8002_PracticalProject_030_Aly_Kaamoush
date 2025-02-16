'''
CST8002 - Programming Language Research Project
Professor: Tyler DeLay
Author: Aly Kaamoush
Date: February 16, 2025
Description: Unit test for adding new record functionality
'''

import unittest
from business.dwelling_manager import DwellingManager
from model.dwelling_record import DwellingRecord

class TestDwellingSystem(unittest.TestCase):
    '''Test case for adding a new record'''
    
    def test_add_new_record(self):
        '''Test if program correctly adds a new record to data structure'''
        print("\nProgram by Aly Kaamoush")
        manager = DwellingManager()
        manager.load_records()
        initial_count = len(manager.records)
        
        # Create test record
        new_record = DwellingRecord()
        new_record.set_csduid(9999)
        new_record.set_csd("Test City")
        new_record.set_period(2025)
        new_record.set_indicator("Test Indicator")
        new_record.set_unit_measure(100.0)
        new_record.set_original_value(200.0)
        
        # Test adding record
        result = manager.add_new_record(new_record)
        self.assertTrue(result)
        
        # Verify record was added
        self.assertEqual(len(manager.records), initial_count + 1)
        added_record = manager.records[-1]
        self.assertEqual(added_record.get_csduid(), 9999)
        self.assertEqual(added_record.get_csd(), "Test City")

if __name__ == '__main__':
    unittest.main()