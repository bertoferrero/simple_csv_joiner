# Simple CSV Joiner

Simple CSV Joiner is a Python tool designed to merge multiple CSV files into a single file. It provides options to specify delimiters and handle decimal formats, making it a flexible solution for combining CSV data. The project is specifically designed to handle large CSV files efficiently, processing input line by line and using a buffered writer to avoid memory overload.

## Features
- Merge all CSV files from a directory or a list of files.
- Retain the header from the first file and ignore headers from subsequent files.
- Support for custom delimiters.
- Option to transform decimal numbers from `3.55` to `3,55`.
- Option to include the source filename in a specified column.
- Efficient memory usage: processes input line by line and employs a buffered writer.

## Requirements
- Python 3.9 or higher

## Installation
Clone the repository to your local machine:
```bash
git clone <repository-url>
cd simple_csv_joiner
```

## Usage

### Command Line Interface
Run the script using the command line:
```bash
python main.py --inputdir <input_directory> --outputfile <output_file> [--delimiter <delimiter>] [--commadecimal <True/False>] [--dump_file_column <column_name>]
```

#### Arguments
- `--inputdir` (required): Path to the directory containing the CSV files to merge.
- `--outputfile` (required): Path to the output CSV file.
- `--delimiter` (optional): Delimiter used in the CSV files. Default is `,`.
- `--commadecimal` (optional): Transform decimal numbers from `3.55` to `3,55`. Default is `False`.
- `--dump_file_column` (optional): Include the source filename (without .csv extension) in the specified column name.

### Examples

#### Basic usage
Merge all CSV files in the `data/` directory into a single file `output.csv`:
```bash
python main.py --inputdir data --outputfile output.csv --delimiter "," --commadecimal False
```

#### Including source filename
Merge all CSV files and include the source filename in a column named "source_file":
```bash
python main.py --inputdir data --outputfile output.csv --dump_file_column source_file
```

#### Complete example with all options
```bash
python main.py --inputdir C:\data\csv_files --outputfile C:\output\merged.csv --delimiter ";" --commadecimal True --dump_file_column trajectory
```

## License
This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.