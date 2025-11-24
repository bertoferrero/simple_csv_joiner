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


import argparse
from lib.csv_joiner import join_csv_from_folder

def main():
    # Load arguments
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--inputdir',
        type=str,
        help='Path the directory where the splited csv are stored',
        required=True
    )
    parser.add_argument(
        '--outputfile',
        type=str,
        help='Output file',
        required=True
    )
    parser.add_argument(
        '--delimiter',
        type=str,
        default=","
    )
    parser.add_argument(
        '--commadecimal',
        type=bool,
        help='Transform decimal numbers from 3.55 to 3,55',
        default=False
    )
    parser.add_argument(
        '--dump_file_column',
        type=str,
        help='Dump the filename in the specified column',
        default=None
    )
    args = parser.parse_args()
    join_csv_from_folder(args.inputdir, args.outputfile, args.delimiter, args.commadecimal, args.dump_file_column)
    

if __name__ == "__main__":
    main()
