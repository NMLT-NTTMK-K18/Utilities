import os
import re

pattern_folder = re.compile(r'^Bai.*$')
pattern_arrays_files = re.compile(r'^.+\.(inp|out)$')
folders = []

for directory in os.listdir('./'):
    if pattern_folder.match(directory):
        folders.append(directory)

for folder in folders:
    os.chdir(folder)
    for file in os.listdir('./'):
        if pattern_arrays_files.match(file):
            os.remove(file)
    os.chdir('../')
