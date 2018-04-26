# Search for a target string in all files in a directory

import os
import string

# Target String is case sensitive in this version
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


for file in files:
    file_name = open(file, "r")
    for line in file_name:
        line_number += 1
        if target_string in line:
            print(f'Target string \"{target_string}\" found on line {line_number} of {file}')
            continue
