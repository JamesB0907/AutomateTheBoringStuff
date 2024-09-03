# The List Data Type:

list_of_numbers = [1, 2, 3, 4]
print(list_of_numbers)

list_of_cats = ['fat', 'orange', 'loud']
print(list_of_cats)

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list_of_lists)

# Getting Individual Values in a List with Indexes:

# like arrays in other languages, Python lists are zero-indexed
print(list_of_cats[0])

print(list_of_cats[1])

print(list_of_cats[2])

# Negative Indexes:

# -1 is the index of the last item in a list, similarly -2 would be the second to last item, and so on
print(list_of_cats[-1])

print('Hello, ' + list_of_cats[0] + ' cat!')

# note: indexes can only be integers, not floats

# Getting a List from Another List with Slices:

list_of_stuff = ['table', 'cat', 'ball', 'dog', 'chair']

# the first index is where the slice starts and the second index is where the slice ends (note that the end index is exclusive, meaning it's own value is not included in the slice)
print(list_of_stuff[1:4])

# if you want to make sure your slice goes to the end of the list, you can leave the second index blank
print(list_of_stuff[1:])

# if you want make sure you get everything from the beginning of the list up to a certain index, you can leave the first index blank
print(list_of_stuff[:3])

# you can use negative indexes in slices as well
print(list_of_stuff[-2:])
print(list_of_stuff[:-2])
print(list_of_stuff[-3:-1])

# Getting a List's Length with the len() Function:

# len() returns the number of items in a list
print(len(list_of_stuff))

# Changing Values in a List with Indexes:

list_of_stuff[1] = 'kitten'
print(list_of_stuff)

# List Concatenation and List Replication:

# you can use the + operator to concatenate lists
list_of_numbers = list_of_numbers + [5, 6, 7, 8]
print(list_of_numbers)

# you can use the * operator to replicate lists
list_of_cats = list_of_cats * 2
print(list_of_cats)

# Removing Values from Lists with del Statements:

# you can use the del statement to remove values from a list
del list_of_stuff[2]
print(list_of_stuff)

# you can also use the del statement to remove a variable from memory
del list_of_stuff
# print(list_of_stuff) # this will raise a NameError because the variable no longer exists

# Working with Lists:

# see all_my_cats.py for an example

# Using for Loops with Lists:

a_new_list_of_stuff = ['London', 'France', 'someone\'s underpants']
for stuff in a_new_list_of_stuff:
    print('I see ' + stuff)

supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

# for stuff in a_new_list_of_stuff iterates over the values in the list, while for i in range(len(supplies)) iterates over the indexes (the numbered positions) of the list

# The in and not in Operators:

'France' in a_new_list_of_stuff
# -> True
'Seattle' not in a_new_list_of_stuff
# -> True
'London' not in a_new_list_of_stuff
# -> False
'France' in supplies
# -> False

# see my_pets.py for a practical example

# The Multiple Assignment Trick:

cat = ['fat', 'orange', 'loud']
size, color, disposition = cat

# cat2 = ['skinny', 'black', 'quiet']
# size2, color2, disposition2, name2 = cat2
# -> ValueError: not enough values to unpack (expected 4, got 3)

# Using the enumerate() Function with Lists:

# the enumerate() function returns two values: the index of the item and the item itself

# supplies = ['pens, 'staplers', 'flamethrowers', 'binders']
for index, item in enumerate(supplies):
    print('Index ' + str(index) + ' in supplies is: ' + item)

# Using the random.choice() and random.shuffle() Functions:

import random
pets = ['Dog', 'Cat', 'Moose']
print(random.choice(pets))

people = ['Alice', 'Bob', 'Carol', 'David']
random.shuffle(people)
print(people)

# Augmented Assignment Operators:
    # spam += 1 is the same as spam = spam + 1
    # spam -= 1 is the same as spam = spam - 1
    # spam *= 1 is the same as spam = spam * 1
    # spam /= 1 is the same as spam = spam / 1
    # spam %= 1 is the same as spam = spam % 1

# Methods:

# Finding a Value in a List with the index() Method:

new_spam = ['hello', 'hi', 'howdy', 'heyas']
new_spam.index('hello')
# -> 0
new_spam.index('heyas')
# -> 3
# new_spam.index('yo')
# -> ValueError: 'yo' is not in list

# duplicated values will return the index of the first occurrence
more_spam = ['Zophie', 'Pooka', 'Fat-tail', 'Pooka']
more_spam.index('Pooka')
# -> 1

# Adding Values to Lists with the append() and insert() Methods:

new_spam.append('yo')
print(new_spam)
# -> ['hello', 'hi', 'howdy', 'heyas', 'yo']

new_spam.insert(1, 'yo')
print(new_spam)
# -> ['hello', 'yo', 'hi', 'howdy', 'heyas', 'yo']

# you cannot use these methods on a str value the way you can with a list value

# Removing Values from Lists with the remove() Method:

new_spam.remove('yo')
print(new_spam)
# -> ['hello', 'hi', 'howdy', 'heyas', 'yo'] Note that it only removes the first occurrence of the value

# Sorting the Values in a List with the sort() Method:

new_spam.sort()
print(new_spam)
# -> ['hello', 'heyas', 'hi', 'howdy', 'yo'] Strings are sorted in alphabetical order

some_numbers = [2, 5, 3.14, 1, -7]
some_numbers.sort()
print(some_numbers)
# -> [-7, 1, 2, 3.14, 5] Numbers are sorted in numerical order including negative numbers

# Note: sort() uses ASCIIbetical order, meaning uppercase letters come before lowercase letters

# if you want to sort in regular alphabetical order, you can pass the key=str.lower argument to the sort() method

capital_and_lower = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
capital_and_lower.sort(key=str.lower)
print(capital_and_lower)
# -> ['Alice', 'ants', 'badgers', 'Bob', 'Carol', 'cats']

# Reversing the Values in a List with the reverse() Method:

capital_and_lower.reverse()
print(capital_and_lower)
# -> ['cats', 'Carol', 'Bob', 'badgers', 'ants', 'Alice']

# Note: reverse() does not sort the list, it simply reverses the order of the values

# Example Program: Magic 8 Ball with a List: see magic_8_ball.py

# Sequence Data Types:

    # list - a value that contains multiple values in an ordered sequence
    # tuple - similar to a list, but immutable
    # str - a sequence of characters
    # range - a sequence of numbers
    # dict - a collection of key-value pairs
    # set - a collection
    # bytes and byte arrays - sequences of bytes
    # bytearray - a mutable version of bytes

# Mutable and Immutable Data Types:

    # mutable - a value that can be changed after it's created
    # immutable - a value that cannot be changed after it's created

# use slicing to mutate a string

cats_name = 'Zophie a cat'
new_cats_name = cats_name[0:7] + 'the' + cats_name[8:12]
print(new_cats_name)
# -> Zophie the cat

# Tuple Data Type:

# a tuple is a list that cannot be changed, it uses parentheses instead of square brackets

new_eggs = ('hello', 42, 0.5)
print(new_eggs[0])
# -> hello

# new_eggs[1] = 99
# -> TypeError: 'tuple' object does not support item assignment

# you can use tuples to store values that should not be changed throughout the life of the program

# if you only have one value in a tuple, you need to include a trailing comma to differentiate it from a value in parentheses

type(('hello',))
# -> <class 'tuple'>
type(('hello'))
# -> <class 'str'>

# Converting Types with the list() and tuple() Functions:

# similar to casting a data type in other languages

print(tuple(['cat', 'dog', 5]))
# -> ('cat', 'dog', 5)
print(list(('cat', 'dog', 5)))
# -> ['cat', 'dog', 5]

# References:

waffle = 42
bacon = waffle
waffle = 99
print(waffle)
# -> 99
print(bacon)
# -> 42

# the second variable can store a snapshot of the value of the first variable, but it does not change when the first variable changes

# the list data type is a reference data type

yet_another_spam = [0, 1, 2, 3, 4, 5]
another_bacon = yet_another_spam
another_bacon[1] = 'hello'
print(yet_another_spam)
# -> [0, 'hello', 2, 3, 4, 5]

# Identity and the id() Function:

# the id() function returns a unique integer for a specific object

toast = 'Hello'
print(id(toast))
# -> 2533566355600

# changing a variable's value does not change the id of the variable unless you print the id of the variable again

toast += ' world!'
print(id(toast))
print(toast)

# Passing References:

def eggs_again(some_parameter):
    some_parameter.append('Hello')
spam_again = [1, 2, 3]
eggs_again(spam_again)
print(spam_again)

# the parameter is a reference to the list, not a copy of the list itself

# The copy Module's copy() and deepcopy() Functions:

import copy
spam_yet_again = ['A', 'B', 'C', 'D']
print(id(spam_yet_again))
# -> 2749981454336
cheese = copy.copy(spam_yet_again)
print(id(cheese))
# -> 2749981454592

cheese[1] = 42
print(spam_yet_again)
# -> ['A', 'B', 'C', 'D']
print(cheese)
# -> ['A', 42, 'C', 'D']

# the copy() function creates a new list with the same values as the original list

# A Short Program: Conway's Game of Life: see conway.py
