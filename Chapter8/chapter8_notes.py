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

response = pyip.inputNum('Enter an integer: ')
print(type(response))

# The min, max, greaterThan, and lessThan Keyword Arguments:

response2 = pyip.inputNum('Enter num: ', min=4)
#If you input '3', you will get a prompt to enter a number greater than 4.
response3 = pyip.inputNum('Enter num: ', greaterThan=4)
#If you input '4', you will get a prompt to enter a number greater than 4.
response4 = pyip.inputNum('Enter num: ', min=4, lessThan=6)
#If you input '6', you will get a prompt to enter a number less than 6.

# The blank Keyword Argument:

response5 = pyip.inputNum('Enter num: ', blank=True)
#If you input nothing, the program will accept it.

# The limit, timeout, and default Keyword Arguments:

response6 = pyip.inputNum(limit=2)
# Only two tries are allowed.
response7 = pyip.inputNum(timeout=10)
# The user has 10 seconds to enter a number.
response8 = pyip.inputNum('Enter num: ', default=0)
# If the user enters nothing, 0 will be the default value.

# The allowRegexes and blockRegexes Keyword Arguments:

response9 = pyip.inputNum(allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zero'])
# The user can enter Roman numerals or the word 'zero'.