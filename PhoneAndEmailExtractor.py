#! python3
# PhoneAndEmailExtractor.py - Finds phone numbers and email addresses on the clipboard

import re
import pyperclip

# test string:
string = str(pyperclip.paste())

# define regex matching rules

phoneRegex = re.compile(r'''
                            (\d{3}|\(\d{3}\))?  # area code
                            (\s|\.|-)?          # separator
                            (\d{3})             # first part of number
                            (\s|\.|-)           # separator
                            (\d{4})             # second part of number
                            ''', re.VERBOSE)

emailRegex = re.compile(r'''
                            [a-zA-Z0-9._%+-]+   # username
                            @                   # @ symbol
                            [a-zA-Z0-9._%+-]+   # domain
                            \.[a-zA-Z]{2,4}     # dot-something
                            ''', re.VERBOSE)

# apply regex rules to the string to create lists of phone numbers and emails

phoneMatches = []

for groups in phoneRegex.findall(string):
    if groups[0]:
        phoneNum = '-'.join([groups[0], groups[2], groups[4]])
    else:
        phoneNum = '-'.join([groups[2], groups[4]])
    phoneMatches.append(phoneNum)

emailMatches = emailRegex.findall(string)

# check for existence of phone numbers and emails, format the output string

output = ''

if len(phoneMatches) > 0:
    output += 'Phone numbers found:\n'
    output += '\n'.join(phoneMatches) + '\n\n'
else:
    output += 'No phone numbers found.\n'

if len(emailMatches) > 0:
    output += 'Email matches found:\n'
    output += '\n'.join(emailMatches)
else:
    output += 'No email matches found.\n'

pyperclip.copy(output)

print(len(phoneMatches), 'phone numbers and', len(emailMatches), 'emails copied.')
