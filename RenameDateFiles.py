#! python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY.

import re       # for matching date styles
import os       # for listing files to check
import sys      # exit script early in case of empty directory
import shutil   # rename files

# define a regular expression for American-style dates
#  with one group for each part so that they can be rearranged
#  using americanRegex.sub()

americanRegex = re.compile(r'(\w*)(\d{2}-)(\d{2}-)(\d{4}\w*)')

# determine the directory to search

print("Enter the directory you would like to search:\n")

response = ''
directory = ''

while True:
    response = input()
    if response == 'exit':
        sys.exit()
    elif os.path.isdir(response):
        directory = response
        os.chdir(directory)
        print('Successfully navigated to %s.\n' % directory)
        break
    else:
        print(response + ' is not a valid path. Try again.\n')

# get a list of files in the directory and check to see if it is nonempty

files = os.listdir(directory)

if not len(files):
    print('No files in %s.' % directory)
    sys.exit()

# find files that match the americanRegex and change to European-style

for ff in files:
    if americanRegex.match(ff):
        print('Changing date style in', ff)
        newName = americanRegex.sub(r'\1\3\2\4', ff)
        newPath = os.path.join(directory, newName)
        oldPath = os.path.join(directory, ff)
        shutil.move(oldPath, newPath)
        print('File now at %s.\n\n' % newPath)
