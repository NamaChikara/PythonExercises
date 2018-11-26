# opens all .txt files in a folder and searches for any line that matches
#  a user-supplied regular expression

import re
import os
import sys

print("Current directory:", os.getcwd())

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

# retrieve any .txt files from the list of files

txtFileReg = re.compile(r'\w+\.txt')

toSearch = []

for ff in files:
    possibleMatch = txtFileReg.match(ff)
    # if not a match, don't try to append
    if possibleMatch:
        toSearch.append(txtFileReg.match(ff)[0])

if len(toSearch) == 0:
    print('No files found.')
    sys.exit()
else:
    print(len(toSearch), '.txt files found')

# ask the user for a regular expression to match

print('Which regular expression would you like to search for?\n')

response = ''

# NOTE: need to turn a response of "r'[a-z]'" into an re.compile(r'[a-z]') instead
#  of the re.compile("r'[a-z]'") it currently is

while True:
    response = input()
    try:
        re.compile(response)
        break
    except re.error:
        print(response, 'is not a valid regular expression. Try again.\n')

print('Searching for %s...' % response)

userRegex = re.compile(response)

# retrieve all instances that match the userRegex

matches = {}

for file in toSearch:
    fileObj = open(os.path.join(directory, file), errors='ignore')
    fileContents = fileObj.read()
    fileMatches = userRegex.findall(fileContents)
    for mm in fileMatches:
        matches.setdefault(mm, 0)
        matches[mm] += 1
    fileObj.close()

# print the results

if len(matches.keys()) == 0:
    print('No matches found.')
else:
    print(len(matches.keys()), ' unique matches found:')
    for mm in matches.keys():
        print(mm, ' was found ', matches[mm], ' times.')
