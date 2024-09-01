#Flow control statements

# Boolean values:

spam = True
print(spam)
# -> True

eggs = False
print(eggs)
# -> False

# True = 2 + 2
# -> SyntaxError: can't assign to keyword

# Comparison operators:
    # == - Equal to
    # != - Not equal to
    # < - Less than
    # > - Greater than
    # <= - Less than or equal to
    # >= - Greater than or equal to

# Boolean operators:
    # and - Both conditions must be True
    # or - Either condition must be True
    # not - Negates the condition

# Binary Boolean operators:
    # & - and
    # | - or
    # ^ - xor
    # ~ - not
    # << - left shift
    # >> - right shift

# Blocks of code:

name = 'Mary'
password = 'swordfish'
if name == 'Mary':
    print('Hello, Mary')
    if password == 'swordfish':
        print('Access granted.')
    else:
        print('Wrong password.')

# the whitespace indicates the execution hierarchy of the code.

# if, else and elif Statements:

# examples of all three

if name == 'Barnabas':
    print('Hello, Barnabas')
elif name == 'Mary':
    print('Hello, Mary')
else:
    print('Hello, stranger')

# see vampire.py, vampire2.py and little_kid.py for more examples

# while Loop Statements:

# with an if statement:
new_spam = 0
if new_spam < 5:
    print('Hello, world.') 
    new_spam = new_spam + 1 # only executes once

print(' ')
# with a while loop:
newer_spam = 0
while newer_spam < 5:
    print('Hello, world.')
    newer_spam = newer_spam + 1 # executes until the statement is false

# more examples in your_name.py

# break Statements:

# example in your_name2.py

# continue Statements:

# example in swordfish.py

# Truthy and Falsey Values:

# Truthy values:
    # True
    # non-zero integers
    # non-zero floats
    # non-empty strings

# Falsey values:
    # False
    # 0
    # 0.0
    # ''
    # []
    # {}

# for Loops and the range() Function:

# see five_times.py for an example

total = 0
for num in range(101):
    total = total + num
print(total)

# An Equivalent while Loop:

print('My name is')
i = 0
while i < 5:
    print('Jimmy Five Times (' + str(i) + ')')
    i = i + 1

# The Starting, Stopping, and Stepping Arguments to range():

for i in range(12, 16):
    print(i)

# With three arguments
for i in range(0, 10, 2): # third argument basically counts by that number
    print(i)

for i in range(2, 10, 2):
    print(f'{i}, ', end='')
print('Who do we appreciate?')

# Importing Modules: