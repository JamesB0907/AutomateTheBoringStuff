#! python3
# Project: Multi-Clipboard Automatic Message
# This program copies a predefined message to the clipboard based on user input.

TEXT = {'agree': 'I agree to the terms and conditions.',
        'busy': 'I am currently busy. Please leave a message.',
        'upsell': 'Would you consider making a monthly donation?',}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    sys.exit()
keyphrase = sys.argv[1] # first command line arg is the keyphrase

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Copied to clipboard:')
    print(TEXT[keyphrase])
else:
    print('There is no text for ' + keyphrase)  

# End of Project: Multi-Clipboard Automatic Message

