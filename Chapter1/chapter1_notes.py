
# Operators:
    # ** - Exponent
    # % - Modulus
    # // - Integer Division/floored quotient (explanation: divides and rounds down to the 'floor')
    # / - Division
    # * - Multiplication
    # - - Subtraction
    # + - Addition

# Syntax error:
# Just as in English language, if you make a syntax error, the computer will not understand you.

#Common Datatypes:
    # int - integer (ie: 1, 2, 3)
    # float - decimal number (ie: 1.0, 2.5, 3.14)
    # str - string (ie: "Hello", "World", "123")

# SyntaxError: EOL while scanning string literal
# Note: Actually throws error 'SyntaxError: unterminated string literal' if you forget to close the string with a quotation mark.
    # print('Hello world!)

# String Concatenation:
print('Hello' + 'World')
# -> HelloWorld
# String Replication:
print('Hello' * 3)
# -> HelloHelloHello
# Incorrect String Concatenation:
# print('Hello' + 5) or print('Hello' * 5)

# Variables:

#Assignment Statements:
spam = 40
print(spam)
# -> 40
eggs = 2
print(eggs + spam)

# Overwriting Variables:
spam = 'Hello'
print(spam)
# -> Hello

spam = 'Goodbye'
print(spam)
# -> Goodbye

# Variable Names:

# Valid variable names:
"""
    current_balance
    currentBalance
    account4
    _42
    TOTAL_SUM
    hello
"""

# Invalid variable names:
    # current-balance (hyphens are not allowed)
    # current balance (spaces are not allowed)
    # 4account (variable names cannot begin with a number)
    # 42 (variable names cannot be a number)
    # TOTAL_$UM (special characters are not allowed)
    # 'hello' (special characters like ' are not allowed either)

# Variable naming convention for Python is snake_case for variable names, but camelCase is also acceptable.

# First Program:
# refer to hello.py module for full code.

# Comments:
# Comments are used to explain what the code does.
# Comments are ignored by the computer when the program is run.

# The print() Function:
# The print() function displays the string value inside the parentheses on the screen.

# The input() Function:
# The input() function waits for the user to type some text on the keyboard and press enter.
# The input() function returns this text as a string value.

# The len() Function:
# The len() function takes a string value and returns an integer value of the string's length.

# Casting with int(), float(), and str():
# The int(), float(), and str() functions will evaluate the value inside the parentheses and return an integer, float, or string value, respectively.
# In our program we use str() to convert the integer value of myAge into a string value so we can concatenate it to the other strings.

# Using the int() function, we can take input from the user and convert it to an integer value.


spam = input()
# -> 42
print(spam)
# -> '42' as a string

spam = int(spam)
print(spam)
# -> 42 as an integer

# You can also use the int() function to convert a float value to an integer value.
int(7.7) # evaluates to 7

# In the hello.py program we cast the addition of 1 to myAge (which is cast as an integer) to a string so we can concatenate it to the other strings.


