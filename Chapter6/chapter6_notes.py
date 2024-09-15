# Manipulating Strings

# String Literals

# string1 = 'This is Alice's cat'  This will cause a syntax error

# Double Quotes

string1 = "This is Alice's cat" # This works fine

# Escape Characters

string2 = 'This is Alice\'s cat' # This will also work fine
print(string2)

# Other Escape Characters:
    # \' - single quote
    # \" - double quote
    # \t - tab
    # \n - newline
    # \\ - backslash

print("Hello there!\nHow are you?\nI\'m doing fine.")

# Raw Strings

print(r'This is Carol\'s cat') # This will print the backslash as well

# Multiline Strings with Triple Quotes

print('''Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob''')

# Multiline Comments

"""This is a test Python program.
Written by Al Sweigart al@inventwithpython.com

This program was designed for Python 3, not Python 2.
"""

def spam():
    """This is a multiline comment to help
    explain what the spam() function does."""
    print('Hello!')

spam()

# Indexing and Slicing Strings

#  ' H e l l o ,  W o  r l  d  ! '
#   0 1 2 3 4 5 6 7 8 9 10 11 12

spam1 = 'Hello, World!'
print(spam1[0]) # H
print(spam1[7]) # W
print(spam1[-1]) # !
print(spam1[0:5]) # Hello
print(spam1[7:12]) # World
print(spam1[:5]) # Hello
print(spam1[7:]) # World!
print(spam1[:]) # Hello, World!
print(spam1[0], spam1[4], spam1[10], spam1[1]) 

# The in and not in Operators with Strings

print('Hello' in spam1) # True
print('Hello' not in spam1) # False

# Putting Strings Inside Other Strings

name = 'Al'
age = 4000
print('Hello, my name is ' + name + ' and I am ' + str(age) + ' years old.')

# String formatting with string interpolation

print('My name is %s and I am %s year old.' % (name, age))

# String Formatting with f-Strings

print(f'My name is {name} and I am {age + 1} years old next year.')

# Useful String Methods: The upper(), lower(), isupper(), and islower() Methods

spam2 = 'Hello, World!'
spam2 = spam2.upper() # HELLO, WORLD!
print(spam2)
print(spam2.islower()) # False
spam2 = spam2.lower() # hello, world!
print(spam2)
print(spam2.isupper()) # False

print('How are you?')
feeling = input()
if feeling.lower() == 'great':
    print('I feel great too.')
else:
    print('I hope the rest of your day is good.')

# The isX() Methods

# isalpha() - returns True if all characters in the string are alphabetic
# isalnum() - returns True if all characters in the string are alphanumeric
# isspace() - returns True if all characters in the string are whitespace
# istitle() - returns True if the string consists only of words that begin with an uppercase letter followed by lowercase letters

print('Hello'.isalpha()) # True
print('Hello123'.isalnum()) # True
print('   '.isspace()) # True
print('Hello World'.istitle()) # True

# See validate_input.py for an example of username validation.

# The startswith() and endswith() Methods

print('Hello, World!'.startswith('Hello')) # True
print('Hello, World!'.endswith('World!')) # True
print('Hello, World!'.endswith('world!')) # False
print('Hello, World!'.startswith('Hi')) # False

# The join() and split() Methods

print(', '.join(['cats', 'dogs', 'rabbits'])) # cats, dogs, rabbits
print('My name is Simon'.split()) # ['My', 'name', 'is', 'Simon']

spam3 ='''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
the is labeled "Milk Experiment."
Please do not drink it.
Sincerely,
Bob'''

print(spam3.split('\n')) # Split by newlines

# Splitting Strings with partition() Method

print('Hello, world!'.partition('w')) # ('Hello, ', 'w', 'orld!')
print('Hello, world!'.partition('world')) # ('Hello, world!', '', '')
# Only executes on the first occurrence of the separator
print('Hello, world!'.partition('o')) # ('Hell', 'o', ' world!')

# Justifying Text with the rjust(), ljust(), and center() Methods

print('Hello'.rjust(10)) # '     Hello'
print('Hello'.rjust(20)) # '               Hello'
print('Hello'.ljust(10)) # 'Hello     '

# Using just with a fill character
print('Hello'.rjust(10, '*')) # '*****Hello'
print('Hello'.ljust(10, '*')) # 'Hello*****'

print('Hello'.center(20)) # '       Hello       '
print('Hello'.center(30, '-')) # '*****Hello*****'

# Anoter example in picnic_table.py

# Removing Whitespace with the strip(), rstrip(), and lstrip() Methods

spam4 = '   Hello, World!   '
print(spam4.strip()) # 'Hello, World!'
print(spam4.rstrip()) # '   Hello, World!'
print(spam4.lstrip()) # 'Hello, World!   '

# You can also specify which chacters on the ends to remove
spam5 = 'SpamSpamBaconSpamEggsSpamSpam'
print(spam5.strip('ampS')) # 'Bacon'

# Numeric Values of Characters with The Ord() and Chr() Functions

# ord() returns the numerical value of a unicode character
print(ord('A')) # 65
print(ord('4')) # 52

# chr() returns the character represented by a unicode value
print(chr(65)) # A
print(chr(52)) # 4

# Copying and Pasting Strings with the pyperclip Module

import pyperclip

pyperclip.copy('Hello, World!')
print(pyperclip.paste()) # Hello, World!

