# Search for a target string in all files in a directory

import os
import string

# Target String is case sensitive
target_string = 'Thundercat'.strip(string.punctuation).strip(string.digits)
path = 'C:\\TestFolder'
files = []
folders = []
line_number = 0

for entry in os.scandir(path):
    if entry.is_dir():
        folders.append(entry.path)
    elif entry.is_file():
        files.append(entry.path)

# using "with open..." ensures the file is closed automatically
for file in files:
    with open(file, "r") as open_file:
        for line in open_file:
            line_number += 1
            if target_string in line:
                print(f'Target string \"{target_string}\" found on line {line_number} of {file}')
                continue
