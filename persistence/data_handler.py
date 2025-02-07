'''
CST8002 - Programming Language Research Project
Professor: Tyler DeLay
Author: Aly Kaamoush
Date: February 16, 2025
Description: Data persistence layer for handling file operations
'''

import pandas as pd
import uuid 
from model.dwelling_record import DwellingRecord

class DataHandler:
    '''Handles all file operations for the dwelling records system'''

    def __init__(self):
        '''Initialize with the dataset filename'''
        self.filename = 'Dwellingunitsdownload.csv'

    def load_data (self, limit=100):
        '''
        Load data from CSV file into DwellingRecord objects
        Args:
            limit: Maximum number of records to load (default 100)
        Returns:
            list of DwellingRecord objects
        '''
        records = []
        try:
            df = pd.read_csv(self.filename)
            data = df.head(limit).values.tolist()

            for row in data:
                record = DwellingRecord()
                record.set_csduid(row[0])
                record.set_csd(row[1])
                record.set_period(row[2])
                record.set_indicator(row[3])
                record.set_unit_measure(row[4])
                record.set_original_value(row[5])
                records.append(record)

        except FileNotFoundError:
            print(f"Error: Cannot find file {self.filename}")
        except Exception as e:
            print(f"Error loading data: {str(e)}")

        return records
    
    def save_data(self, records):
        '''
        Save records to a new CSV file with UUID filename
        Args:
            records: list of DwellingRecord objects
        Returns:
            filename of the saved file
        '''

        try:
            # Generate unique filename using UUID API
            unique_id = uuid.uuid4() # Generate a unique identifier
            filename = f"dwelling_data_{unique_id}.csv"

            data = []
            for record in records:
                data.append({
                    'CSDUID': record.get_csduid(),
                    'CSD': record.get_csd(),
                    'Period': record.get_period(),
                    'IndicatorSummaryDescription': record.get_indicator(),
                    'UnitOfMeasure': record.get_unit_measure(),
                    'OriginalValue': record.get_original_value()
                })

            df = pd.DataFrame(data)
            df.to_csv(filename, index=False)
            return filename

        except Exception as e:
            print(f"Error saving data: {str(e)}")
        return None