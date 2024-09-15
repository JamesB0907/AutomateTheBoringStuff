# Dictionaries and Structuring Data

# Dictionary data type

# A Series of key-value pairs, similar to objects in JavaScript
myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}

myCat['size']

print('My cat has ' + myCat['color'] + ' fur.')

# Dictionaries vs. Lists

# Lists are ordered:
spam = ['cats', 'dogs', 'moose']
bacon = ['dogs', 'moose', 'cats']
spam == bacon # False

# Dictionaries are unordered:
eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
eggs == ham # True

new_spam = {'name': 'Zophie', 'age': 7}
# new_spam['color'] # KeyError

#see birthdays.py for a dictionary example

# The keys(), values(), and items() Methods

# values() method
spam3 = {'color': 'red', 'age': 42}
for v in spam3.values():
    print(v) # red, 42

# keys() method
for k in spam3.keys():
    print(k) # color, age

# items() method
for i in spam3.items():
    print(i) # ('color', 'red'), ('age', 42)

# Checking Whether a Key or Value Exists in a Dictionary

spam4 = {'name': 'Zophie', 'age': 7}
'name' in spam4.keys() # True
'Zophie' in spam4.values() # True
'color' in spam4.keys() # False
'color' not in spam4.keys() # True
'color' in spam4 # False

# The get() Method

picnic_items = {'apples': 5, 'cups': 2}
'I am bringing ' + str(picnic_items.get('cups', 0)) + ' cups.' # I am bringing 2 cups.
'I am bringing ' + str(picnic_items.get('eggs', 0)) + ' eggs.' # I am bringing 0 eggs.

# The setdefault() Method

# Setting a value in a dictionary
spam5 = {'name': 'Pooka', 'age': 5}
if 'color' not in spam5:
    spam5['color'] = 'black'

# Using setdefault()
spam6 = {'name': 'Pooka', 'age': 5}
spam6.setdefault('color', 'black') # 'black'
for l in spam6.items():
    print(l) # ('name', 'Pooka'), ('age', 5), ('color', 'black')

message = 'It was a bright cold day in April, and the clocks were thirteen.'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] += 1
print(count)

# Pretty Printing

import pprint
for character2 in message:
    count.setdefault(character2, 0)
    count[character2] += 1
pprint.pprint(count)

# Using Data Structures to Model Real-World Things

# A tic-tac-toe board in tic_tac_toe.py

# Nested Dictionaries and Lists

all_guests = {'Alice': {'apples': 5, 'pretzels': 12},
              'Bob': {'ham sandwiches': 3, 'apples': 2},
              'Carol': {'cups': 3, 'apple pies': 1}}
def total_brought(guests, item):
    num_brought = 0
    for k, v in guests.items():
        num_brought = num_brought + v.get(item, 0)
    return num_brought
print('Number of things being brought:')
print(' - Apples         ' + str(total_brought(all_guests, 'apples')))
print(' - Cups           ' + str(total_brought(all_guests, 'cups')))
print(' - Cakes          ' + str(total_brought(all_guests, 'cakes')))
print(' - Ham Sandwiches ' + str(total_brought(all_guests, 'ham sandwiches')))
print(' - Apple Pies     ' + str(total_brought(all_guests, 'apple pies')))






