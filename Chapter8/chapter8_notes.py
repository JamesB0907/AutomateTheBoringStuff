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
# This will also except roman numerals with incorrect order

# You can instead specify a list of regular expressions that the input must not match by using the blockRegexes keyword argument.

response10 = pyip.inputNum(blockRegexes=[r'[02468]$'])
# 42 will be rejected because it ends in an even number.

## If you specify both allowRegexes and blockRegexes, the allow list is checked first, and then the block list is checked.

response11 = pyip.inputStr(allowRegexes=[r'caterpillar', 'category'], blockRegexes=[r'cat'])
# cat is invalid
# catastrophe is invalid
# caterpillar is valid
# category is valid

# Passing a Custom Validation Function to inputCustom():

# Creating a custom function to validate if the input adds up to 10:

# see adds_up_to_ten.py for a custom validation function

# Project: How to Keep an Idiot Busy for Hours:

# This project will create a program that will keep the user busy for hours. The program will ask the user to enter a number and will only accept the number 5. If the user enters anything else, the program will keep asking the user to enter a number until they enter 5.

# see idiot.py for the code

# Project: Multiplication Quiz:

# This project will create a multiplication quiz that will ask the user 10 multiplication questions. The user will have 8 seconds to answer each question. If the user answers the question correctly, the program will display 'Correct!' and move on to the next question. If the user answers the question incorrectly or runs out of time, the program will display 'Incorrect!' and move on to the next question. At the end of the quiz, the program will display the number of questions the user answered correctly and the total number of questions.

# see multiplication_quiz.py for the code

# Summary:

# The PyInputPlus module has functions to validate input.
# The inputStr(), inputNum(), inputChoice(), inputMenu(), inputDatetime(), inputYesNo(), inputBool(), inputFilepath(), and inputPassword() functions will validate input.
# The min, max, greaterThan, lessThan, blank, limit, timeout, default, allowRegexes, and blockRegexes keyword arguments can be used to validate input.
# You can create custom validation functions and pass them to the inputCustom() function.