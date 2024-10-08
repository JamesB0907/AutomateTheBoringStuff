# Chapter 7 Notes

# Finding Patterns of Text Without Regular Expressions

# See is_phone_number.py for an example of finding a phone number in a string

# Finding Patterns of Text with Regular Expressions

# Regular expressions are a powerful tool for various kinds of string manipulation

# Creating Regex Objects

# import the regex module with import re
import re

phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

# Matching Regex Objects

# use the search() method to search for a match

mo = phone_num_regex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())

# Review of Regular Expression Matching

# More Pattern Matching with Regular Expressions

# Grouping with Parentheses
another_phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
another_mo = another_phone_num_regex.search('My number is 415-555-4242.')
another_mo.group(1)
another_mo.group(2)
another_mo.group(0)
another_mo.group()
# If you would like to retrieve all the groups at once, use the groups() method
another_mo.groups() # will return ('415', '555-4242')
area_code, main_number = another_mo.groups()
print(area_code) # prints 415
print(main_number) # prints 555-4242

# \ with a special character will allow you to detect them
# \. \^ \$ \* \+ \? \{ \} \[ \] \\ \| \( \)

# Matching Multiple Groups with the Pipe

# The | character is called a pipe. You can use it to match one of many expressions

hero_regex = re.compile(r'Batman|Tina Fey')
mo1 = hero_regex.search('Batman and Tina Fey.')
mo1.group() # will return Batman
mo2 = hero_regex.search('Tina Fey and Batman.')
mo2.group() # will return Tina Fey

# You can also use the pipe to match multiple patterns

bat_regex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = bat_regex.search('Batmobile lost a wheel')
mo.group() # will return Batmobile
mo.group(1) # will return mobile

# Optional Matching with the Question Mark

# The ? character can be used to match zero or one of the preceding group

bat_regex2 = re.compile(r'Bat(wo)?man')
mo3 = bat_regex2.search('The Adventures of Batman')
mo3.group() # will return Batman
mo4 = bat_regex2.search('The Adventures of Batwoman')
mo4.group() # will return Batwoman

