'''
CST8002 - Programming Language Research Project
Professor: Tyler DeLay
Author: Aly Kaamoush
Date: March 16, 2025
Description: Unit test for polymorphic record display functionality
'''

import unittest
from model.dwelling_record import DwellingRecord, DetailedDwellingRecord, SummaryDwellingRecord

class TestPolymorphicDisplay(unittest.TestCase):
    '''Test case for polymorphic display functionality'''
    
    def setUp(self):
        '''Set up test fixtures'''
        print("\nProgram by Aly Kaamoush")
        
        # Create test records of different types
        self.base_record = DwellingRecord()
        self.base_record.set_csduid(1001)
        self.base_record.set_csd("Ottawa")
        self.base_record.set_period(2024)
        self.base_record.set_indicator("Housing Units")
        self.base_record.set_unit_measure("Count")
        self.base_record.set_original_value(75.5)
        
        self.detailed_record = DetailedDwellingRecord()
        self.detailed_record.set_csduid(1001)
        self.detailed_record.set_csd("Ottawa")
        self.detailed_record.set_period(2024)
        self.detailed_record.set_indicator("Housing Units")
        self.detailed_record.set_unit_measure("Count")
        self.detailed_record.set_original_value(75.5)
        
        self.summary_record = SummaryDwellingRecord()
        self.summary_record.set_csduid(1001)
        self.summary_record.set_csd("Ottawa")
        self.summary_record.set_period(2024)
        self.summary_record.set_indicator("Housing Units")
        self.summary_record.set_unit_measure("Count")
        self.summary_record.set_original_value(75.5)
        
    def test_polymorphic_display(self):
        '''Test if different record types generate different formatted outputs'''
        # Test base record format
        base_output = self.base_record.format_for_display()
        self.assertIn("CSDUID: 1001", base_output)
        self.assertIn("CSD: Ottawa", base_output)
        
        # Test detailed record format has additional elements
        detailed_output = self.detailed_record.format_for_display()
        self.assertIn("DETAILED RECORD VIEW", detailed_output)
        self.assertIn("Growing", detailed_output)  # Should indicate growth
        
        # Test summary record format is concise
        summary_output = self.summary_record.format_for_display()
        self.assertIn("SUMMARY:", summary_output)
        self.assertTrue(len(summary_output) < len(base_output))
        
        # Verify each subclass implements the same method differently
        self.assertNotEqual(base_output, detailed_output)
        self.assertNotEqual(base_output, summary_output)
        self.assertNotEqual(detailed_output, summary_output)

if __name__ == '__main__':
    unittest.main()