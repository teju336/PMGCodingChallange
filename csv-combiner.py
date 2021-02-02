# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 09:56:03 2021

@author: tejas
"""

import argparse
import sys
from csv_manager import CsvObj

'''
Argument Handling
'''
parser = argparse.ArgumentParser(prog='csv-combiner.py',
                                 description='Combine multiple csv files with same columns. '
                                 'Adds an extra column of the filename the object belongs to.')
parser.add_argument('files', metavar='files', type=argparse.FileType('r'), nargs='+',
                    help='CSV files to be combined into one big CSV file.')
args = parser.parse_args()

'''
File Management
'''

# Turn all files into CSV Objects
fileList = [CsvObj(file.name) for file in args.files]

'''
Verify all the columns are the same
'''
for file in fileList:
    file.set_columns()

name_of_column = ""
try:
    name_of_column = fileList[0].get_columns()
    for file in fileList:
        if name_of_column != file.get_columns():
            raise ValueError("Invalid column names.", name_of_column, file.get_columns(),file.get_name())
except ValueError as err:
    print(err.args)
    sys.exit("Check the CSV files to see that all the columns match up.")

'''
Writing input files to Stdout
'''

# Initialize column names in final file
sys.stdout.write(name_of_column.strip() + ',\"filename\"\n')

# Append each file to the output file
for file in fileList:
    file.write_to_file()