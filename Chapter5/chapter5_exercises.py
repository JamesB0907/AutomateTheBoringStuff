# 1. What does the code for an empty dictionary look like?

empty_dictionary = {}

# 2. What does a dictionary value with a key 'foo' and a value 42 look like?

dictionary_value = {'foo': 42}

# 3. What is the main difference between a dictionary and a list?

# List are ordered and dictionaries are unordered. Also lists are a set of single values and dictionaries are key-value pairs.

# 4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?

# You will get a KeyError because 'foo' is not in the dictionary.

# 5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?

spam = {'cat': 1, 'dog': 2}
print('cat' in spam) # True
# 'cat' in spam returns a truth value if it finds the key 'cat' in spam keys

spam2 = {1: 'cat'}
print('cat' in spam2) # False
# It only works for keys of the dictionary unless you use .values()
print('cat' in spam2.values()) # True

# 6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?

# They will essentially do the same thing. The first one will look for 'cat' in the keys and the second one will look for 'cat' in the keys.

# 7. What is a shortcut for the following code?

if 'color' not in spam:
    spam['color'] = 'black'

spam.setdefault('color', 'black')

# 8. What module and function can be used to “pretty print” dictionary values?

import pprint
pprint.pprint(spam)

# Practice Projects:

# Chess Dictionary Validator: see chess_validator.py

