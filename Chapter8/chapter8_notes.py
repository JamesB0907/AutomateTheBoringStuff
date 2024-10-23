# Automate the Boring Stuff Chapter 8 Notes

# Input Validation:

# Typical input validation will look like this:

while True:
    print('Enter your age:')
    age = input()
    try:
        age = int(age)
    except:
        print('Please use numeric digits.')
        continue
    if age < 1:
        print('Please enter a positive number.')
        continue
    break
print(f'Your age is {age}.')

# The code above will keep asking the user to enter their age until they enter a positive number.

# The PyInputPlus Module:

# The PyInputPlus module is a module that has functions to validate input. You can install it with pip: pip install pyinputplus


# Here is the list of functions that PyInputPlus has:

    # inputStr() will ensure the user enters a string value
    # inputNum() will ensure the user enters a number value
    # inputChoice() will ensure the user enters one of the provided choices
    # inputMenu() will ensure the user enters one of the provided menu choices
    # inputDatetime() will ensure the user enters a date and time value
    # inputYesNo() will ensure the user enters a yes or no value
    # inputBool() will ensure the user enters a boolean value
    # inputFilepath() will ensure the user enters a file path
    # inputPassword() will ensure the user enters a password value

import pyinputplus as pyip

response = pyip.inputNum()

