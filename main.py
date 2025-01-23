'''
CST8002 - Programming Language Research Project
Professor:  Tyler DeLay
Author: Aly Kaamoush
Date: January 26, 2025
Description: Main Program file for reading and displaying dwelling unit data
'''
from dwelling_record import DwellingRecord
import pandas as pd

def read_dwelling_data(filename):
    '''
    Open and read the CSV file using both File-IO and pandas API.
    Uses error handling for file operations.
    '''
    my_records = []

    try:
        with open(filename, 'r') as file:

            data = pd.read_csv(filename)

            first_few = data.head()

            rows = first_few.values.tolist()

            for row in rows:
                new_record = DwellingRecord()

                new_record.set_csduid(row[0])
                new_record.set_csd(row[1])
                new_record.set_period(row[2])
                new_record.set_indicator(row[3])
                new_record.set_unit_measure(row[4])
                new_record.set_original_value(row[5])

                my_records.append(new_record)

    except FileNotFoundError:
        print("Error: can't find the csv file")
    except Exception as e:
        print ("Something went wrong: ", e)

    return my_records

def main():
    '''
    Main function to run the program.
        
        to Display author name (always visible),
        Read CSV data using File-IO and pandas API,
        Create record objects from data,
        and Display records with formatting
    '''    
    records = read_dwelling_data('Dwellingunitsdownload.csv')

    if records:
        print ("\nDisplying Dweilling Records: ")
        print ("=" * 50, "Program by Aly Kaamoush")

        for record in records:
            print (f"\nCSDUID: {record.get_csduid()}")
            print (f"CSD: {record.get_csd()}")
            print (f"Period: {record.get_period()}")
            print (f"IndicatorSummaryDescription: {record.get_indicator()}")
            print (f"Unit Of Measure: {record.get_unit_measure()}")
            print (f"Original Value: {record.get_original_value()}")
            print ("_" * 50, "Program by Aly Kaamoush")

if __name__ == "__main__":
    ''' Conditional block to run main() function '''
    main()



