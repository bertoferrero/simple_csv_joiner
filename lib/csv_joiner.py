# Copyright 2025 Alberto Ferrero López
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import os
import glob
import csv
from lib.bufferedcsvfilewriter import BufferedCsvFileWriter


def join_csv_from_folder(input_dir: str, output_file: str, delimiter: str, commadecimal: bool):
    """
    Join all the csv files from a directory into a single csv file.
    The first row of the first file will be used as header. The rest of the files will be appended to it.
    The header of the rest of the files will be ignored.

    Args:
        input_dir (str): Path to the directory where the csv files are stored.
        output_file (str): Path to the output file.
        delimiter (str): Delimiter used in the csv files.
        commadecimal (bool): If True, transform decimal numbers from 3.55 to 3,55.

    """
    #Check if the input folder exists
    if not os.path.isdir(input_dir):
        raise ValueError(f"Defined input path does not exists: {input_dir}")
    
    #List all the csv files from that directory
    csv_files = glob.glob(os.path.join(input_dir, "*.csv"))
    if len(csv_files) == 0:
        raise ValueError("No csv file has been found in the input directory")

    #Request to join all of them
    join_csv_from_list(csv_files, output_file, delimiter, commadecimal)

def join_csv_from_list(input_csv_files: list[str], output_file: str, delimiter: str, commadecimal: bool):

    """
    Join all the csv files from a list into a single csv file.
    The first row of the first file will be used as header. The rest of the files will be appended to it.
    The header of the rest of the files will be ignored.

    Args:
        input_csv_files (list[str]): List of paths to the csv files to be joined.
        output_file (str): Path to the output file.
        delimiter (str): Delimiter used in the csv files.
        commadecimal (bool): If True, transform decimal numbers from 3.55 to 3,55.

    """

    #Check parameters values        
    output_dir = os.path.dirname(output_file)
    if output_dir and not os.path.exists(output_dir):
        raise ValueError(f"Defined ouput path does not exists: {output_dir}")
    if os.path.exists(output_file):
        raise ValueError(f"Ouput file already exists: {output_file}")
    
    if len(input_csv_files) == 0:
        raise ValueError("Input csv files list is empty")
    for input_file in input_csv_files:
        if not (os.path.exists(input_file) and os.path.isfile(input_file)):
            raise ValueError(f"This file does not exists: {input_file}")
        
    
    #Read and combine all csv files
    csv_header = True
    csv_writter = BufferedCsvFileWriter(output_file)
    for input_file in input_csv_files:
        with open(input_file, newline='') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=delimiter)
            for i, row in enumerate(csv_reader):
                # Write only the header from the first file
                if i == 0 and not csv_header:
                    continue
                csv_header = False
                row = fix_row(row, commadecimal=commadecimal)
                csv_writter.write(row)
    csv_writter.close()


def fix_row(row:list[str], commadecimal: bool):
    """
    Fix the row to be written in the csv file.

    Args:
        row (list[str]): The row to be fixed.
        commadecimal (bool): If True, transform decimal numbers from 3.55 to 3,55.

    Returns:
        list[str]: The fixed row.
    """

    # Remove leading and trailing whitespace from each element in the row
    if commadecimal:
        for i, value in enumerate(row):
            try:
                # Attempt to parse the value as a float
                float(value)
                # Replace '.' with ',' if it's a decimal number
                if '.' in value or 'E' in value.upper():
                    row[i] = value.replace('.', ',')
            except ValueError:
                # Skip values that cannot be parsed as float
                pass

    return row