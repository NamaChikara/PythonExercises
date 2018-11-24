#! python3
# adds Wikipedia bullet points to the start of each lin
#  of text on the clipboard

import pyperclip

text = pyperclip.paste()

lines = text.split('\n')

for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

text = '\n'.join(lines)

pyperclip.copy(text)
