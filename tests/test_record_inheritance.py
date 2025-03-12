'''
CST8002 - Programming Language Research Project
Professor: Tyler DeLay
Author: Aly Kaamoush
Date: February 27, 2025
Description: Unit test for inheritance and overridden method formats
'''

import unittest
from model.dwelling_record import DwellingRecord, DetailedDwellingRecord, SummaryDwellingRecord

class TestRecordInheritance(unittest.TestCase):
    '''Test case for inheritance and overridden method correctness'''
    
    def setUp(self):
        '''Set up test fixtures'''
        print("\nProgram by Aly Kaamoush")
        
    def test_inheritance_structure(self):
        '''Test that the classes have the correct inheritance relationship'''
        # Create instances
        base_record = DwellingRecord()
        detailed_record = DetailedDwellingRecord()
        summary_record = SummaryDwellingRecord()
        
        # Test inheritance relationships
        self.assertTrue(isinstance(detailed_record, DwellingRecord))
        self.assertTrue(isinstance(summary_record, DwellingRecord))
        
        # Test that they're different classes
        self.assertFalse(isinstance(base_record, DetailedDwellingRecord))
        self.assertFalse(isinstance(base_record, SummaryDwellingRecord))
        self.assertFalse(isinstance(detailed_record, SummaryDwellingRecord))
        self.assertFalse(isinstance(summary_record, DetailedDwellingRecord))
    
    def test_overridden_methods(self):
        '''Test that the overridden format_for_display methods are correctly implemented'''
        # Create records with identical data
        test_data = {
            'csduid': 1001,
            'csd': 'Ottawa',
            'period': 2024,
            'indicator': 'Housing Units',
            'unit_measure': 'Count',
            'original_value': 75.5
        }
        
        # Create and populate records
        base_record = DwellingRecord()
        detailed_record = DetailedDwellingRecord()
        summary_record = SummaryDwellingRecord()
        
        for record in [base_record, detailed_record, summary_record]:
            record.set_csduid(test_data['csduid'])
            record.set_csd(test_data['csd'])
            record.set_period(test_data['period'])
            record.set_indicator(test_data['indicator'])
            record.set_unit_measure(test_data['unit_measure'])
            record.set_original_value(test_data['original_value'])
        
        # Test base record format follows standard format
        base_output = base_record.format_for_display()
        self.assertIn("CSDUID: 1001", base_output)
        self.assertIn("CSD: Ottawa", base_output)
        self.assertIn("Period: 2024", base_output)
        
        # Test detailed record format follows detailed specification
        detailed_output = detailed_record.format_for_display()
        self.assertIn("DETAILED RECORD VIEW", detailed_output)
        self.assertIn("Location ID: 1001 - Ottawa", detailed_output)
        self.assertIn("Growing", detailed_output)  # Check for growth indicator
        
        # Test summary record format follows summary specification
        summary_output = summary_record.format_for_display()
        self.assertIn("SUMMARY:", summary_output)
        self.assertIn("Ottawa (2024)", summary_output)
        self.assertIn("Housing Units", summary_output)
        
        # Verify that each class implements the format differently
        self.assertNotEqual(base_output, detailed_output)
        self.assertNotEqual(base_output, summary_output)
        self.assertNotEqual(detailed_output, summary_output)
    
    def test_polymorphic_behavior(self):
        '''Test polymorphic behavior using a list of the base type'''
        # Create records with identical data
        test_data = {
            'csduid': 1001,
            'csd': 'Ottawa',
            'period': 2024,
            'indicator': 'Housing Units',
            'unit_measure': 'Count',
            'original_value': 75.5
        }
        
        # Create and populate records
        base_record = DwellingRecord()
        detailed_record = DetailedDwellingRecord()
        summary_record = SummaryDwellingRecord()
        
        for record in [base_record, detailed_record, summary_record]:
            record.set_csduid(test_data['csduid'])
            record.set_csd(test_data['csd'])
            record.set_period(test_data['period'])
            record.set_indicator(test_data['indicator'])
            record.set_unit_measure(test_data['unit_measure'])
            record.set_original_value(test_data['original_value'])
        
        # Create a list of the base type (demonstrates polymorphism)
        record_list = [base_record, detailed_record, summary_record]
        
        # Each call to format_for_display should use the appropriate overridden method
        outputs = [record.format_for_display() for record in record_list]
        
        # Verify each output is different despite calling the same method name
        self.assertIn("CSDUID:", outputs[0])  # Base record format
        self.assertIn("DETAILED RECORD VIEW", outputs[1])  # Detailed record format
        self.assertIn("SUMMARY:", outputs[2])  # Summary record format
        
        # Each output should be unique
        self.assertEqual(len(set(outputs)), 3)  # 3 different outputs

if __name__ == '__main__':
    unittest.main()