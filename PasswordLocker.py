#! python3
# an insecure password locker program
# Note: to run this from command line, navigate to the containing folder.
#  Next, type "python PasswordLocker.py key" where key is one of the key
#  values in the PASSWORDS dict

import sys
import pyperclip  # a cross-platform clipboard module for python

PASSWORDS = {'email': '123',
             'blog': '456'}

if len(sys.argv) < 2 or len(sys.argv) > 3:
    print('Bad number of arguments.')
    sys.exit()
# since the first argument is the file name, 2 arguments is asking
#  to access the value associated to the second argument; 3 arguments
#  is asking to create a (key, value) with the 2nd 2 arguments
elif len(sys.argv) == 2:
    account = sys.argv[1]  # first command line arg is the account name
    if account in PASSWORDS:
        pyperclip.copy(PASSWORDS[account])
        print('Password for ' + account + ' copied to clipboard.')
    else:
        print('There is no account named ' + account)
else:
    newaccount = sys.argv[1]
    newpassword = sys.argv[2]
    if newaccount in PASSWORDS:
        print('Password for ' + newaccount + ' updated to '
              + newpassword + '.')
    else:
        print('Password for ' + newaccount + ' added to PASSWORDS.')
    PASSWORDS[newaccount] = newpassword
    pyperclip.copy(newpassword)
