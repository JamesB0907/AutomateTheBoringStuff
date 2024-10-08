#! python3
# bullet_points_adder.py - Adds Wikipedia bullet points to the start of each line of text on the clipboard.

import pyperclip

text = pyperclip.paste()
lines = text.split('\n') # Split the text into lines
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]
text = '\n'.join(lines) # Join the lines back together
pyperclip.copy(text)
print(pyperclip.paste()) # Print the modified text to the console

