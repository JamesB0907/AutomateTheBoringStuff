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

# with the phone number example, you can use the ? to match phone numbers with or without an area code

phone_regex = re.compile('r(\d\d\d-)?\d\d\d-\d\d\d\d')
mo5 = phone_regex.search('My number is 415-555-4242')
mo5.group() # will return 415-555-4242
mo6 = phone_regex.search('My number is 555-4242')
mo6.group() # will return 555-4242

# Matching Zero or More with the Star

# The * character can be used to match zero or more of the preceding group

bat_regex3 = re.compile(r'Bat(wo)*man')
mo7 = bat_regex3.search('The Adventures of Batman')
mo7.group() # will return Batman
mo8 = bat_regex3.search('The Adventures of Batwoman')
mo8.group() # will return Batwoman
mo9 = bat_regex3.search('The Adventures of Batwowowowoman')
mo9.group() # will return Batwowowowoman

# Matching One or More with the Plus

# The + character can be used to match one or more of the preceding group

bat_regex4 = re.compile(r'Bat(wo)+man')
mo10 = bat_regex4.search('The Adventures of Batwoman')
mo10.group() # will return Batwoman
mo11 = bat_regex4.search('The Adventures of Batwowowowoman')
mo11.group() # will return Batwowowowoman
mo12 = bat_regex4.search('The Adventures of Batman')
mo12 == None # will return True

# Matching Specific Repetitions with Braces

# The {x} character can be used to match x number of the preceding group

ha_regex = re.compile(r'(Ha){3}')
mo13 = ha_regex.search('HaHaHa')
mo13.group() # will return HaHaHa
mo14 = ha_regex.search('Ha')
mo14 == None # will return True

# Greedy and Non-Greedy Matching

# Python's regular expressions are greedy by default, which means that in ambiguous situations they will match the longest string possible

greedy_ha_regex = re.compile(r'(Ha){3,5}')
mo15 = greedy_ha_regex.search('HaHaHaHaHa')
mo15.group() # will return HaHaHaHaHa
nongreedy_ha_regex = re.compile(r'(Ha){3,5}?')
mo16 = nongreedy_ha_regex.search('HaHaHaHaHa')
mo16.group() # will return HaHaHa

# The ? character can be used to make the matching nongreedy

# The findall() Method

# The findall() method will return all matches in a list

# search() will return a match object of the first occurrence

phone_num_regex2 = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phone_num_regex2.search('Cell: 415-555-9999 Work: 212-555-0000')
mo.group() # will return 415-555-9999

#findall() on the other hand will return a list of all matches

phone_num_regex3 = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo2 = phone_num_regex3.findall('Cell: 415-555-9999 Work: 212-555-0000')
mo2 # will return ['415-555-9999', '212-555-0000']

# findall() returns a list of strings on a regex with no groups
# findall() returns a list of tuples on a regex with groups

# Character Classes:

    # \d - Any numeric digit from 0 to 9
    # \D - Any character that is not a numeric digit from 0 to 9
    # \w - Any letter, numeric digit, or the underscore character
    # \W - Any character that is not a letter, numeric digit, or the underscore character
    # \s - Any space, tab, or newline character
    # \S - Any character that is not a space, tab, or newline character

# Making Your Own Character Classes:

# You can create your own character classes with square brackets

vowel_regex = re.compile(r'[aeiouAEIOU]')
vowel_regex.findall('RoboCop eats baby food. BABY FOOD.') # will return ['o', 'o', 'o', 'e', 'a', 'o', 'o', 'A', 'O', 'O']

# You can include a range using a hyphen

# Placing a caret chacacter (^) just after the opening square bracket will match any character that is not in the character class

consonant_regex = re.compile(r'[^aeiouAEIOU]')
consonant_regex.findall('RoboCop eats baby food. BABY FOOD.') # will return ['R', 'b', 'C', 'p', 't', 's', 'b', 'b', 'y', 'f', 'd', '.', 'B', 'B', 'Y', 'F', 'D', '.']

# The Caret and Dollar Sign Characters:

# Using a caret (^) at the start of a regex will indicate that a match must occur at the beginning of the searched text

# Using a dollar sign ($) at the end of a regex will indicate that a match must occur at the end of the searched text

begins_with_hello = re.compile(r'^Hello')
begins_with_hello.search('Hello world!') # will return a match object
begins_with_hello.search('He said hello.') == None # will return True

ends_with_number = re.compile(r'\d$')
ends_with_number.search('Your number is 42') # will return a match object, in this case the number 2 since it is the single last character and is a digit
ends_with_number.search('Your number is forty two.') == None # will return True

# You can match one or more digits by using the + character
# The following regex matches strings that both begin and end with one or more numeric characters

whole_string_is_num = re.compile(r'^\d+$')
whole_string_is_num.search('1234567890') # will return a match object
whole_string_is_num.search('12345xyz67890') == None # will return True
whole_string_is_num.search('12 34567890') == None # will return True

# The Wildcard Character:

# The . character will match any character except for a newline

at_regex = re.compile(r'.at')
at_regex.findall('The cat in the hat sat on the flat mat.') # will return ['cat', 'hat', 'sat', 'lat', 'mat']

# Matching Everything with Dot-Star:

# The .* will match any single character except for a newline AND zero or more of the preceding character

name_regex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo17 = name_regex.search('First Name: Al Last Name: Sweigart')
mo17.group(1) # will return Al
mo17.group(2) # will return Sweigart

# The .* is greedy, so it will match as much text as possible

# To match any and all text in a nongreedy fashion, use the .*?

non_greedy_regex = re.compile(r'<.*?>')
mo18 = non_greedy_regex.search('<To serve man> for dinner.>')
mo18.group() # Will return '<To serve man>'
greedy_regex = re.compile(r'<.*>')
mo19 = greedy_regex.search('<To serve man> for dinner.>')
mo19.group() # Will return '<To serve man> for dinner.>'

# Matching Newlines with the Dot Character:

# The . character will match any character except for a newline
# To match any character including a newline, use the re.DOTALL as the second argument to re.compile()

no_newline_regex = re.compile('.*')
no_newline_regex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group() # will return 'Serve the public trust.'
newline_regex = re.compile('.*', re.DOTALL)
newline_regex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group() # will return 'Serve the public trust.\nProtect the innocent.\nUphold the law.'

# Review of Regex Symbols

    # ? - matches zero or one of the preceding group
    # * - matches zero or more of the preceding group
    # + - matches one or more of the preceding group
    # {n} - matches exactly n of the preceding group
    # {n,} - matches n or more of the preceding group
    # {,m} - matches 0 to m of the preceding group
    # {n,m} - matches at least n and at most m of the preceding group
    # {n,m}? or *? or +? - performs a nongreedy match of the preceding group
    # ^spam - means the string must begin with spam
    # spam$ - means the string must end with spam
    # . - matches any character except newline characters
    # \d, \w, and \s - match a digit, word, or space character, respectively
    # \D, \W, and \S - match anything except a digit, word, or space character, respectively
    # [abc] - matches any character between the brackets (such as a, b, or c)
    # [^abc] - matches any character that isn't between the brackets

# Case-Insensitive Matching:

# re.IGNORECASE is used as the second argument to re.compile() to make the matching case-insensitive

robocop = re.compile(r'robocop', re.I)
robocop.search('RoboCop is part man, part machine, all cop.').group() # 'RoboCop
robocop.search('ROBOCOP protects the innocent.').group() # 'ROBOCOP
robocop.search('Al, why does your programming book talk about robocop so much?').group() # 'robocop'

# Substituting Strings with the sub() Method:

# The sub() method is used to substitute strings

names_regex = re.compile(r'Agent \w+')
print(names_regex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')) # will return 'CENSORED gave the secret documents to CENSORED.'

# You can use \1, \2, \3, etc. in the first argument to sub() to substitute text from the matched group

agent_names_regex = re.compile(r'Agent (\w)\w*')
agent_names_regex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.') # will return 'A**** told C**** that E**** knew B**** was a double agent.'

# Managing Complex Regexes:

# The re.VERBOSE argument allows you to add whitespace and comments to the string passed to re.compile()

# Without verbose mode
phone_regex4 = re.compile(r'((\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?')

# With verbose mode
phone_regex5 = re.compile(r'''(
    (\d{3}|\(\d{3}\))? # area code
    (\s|-|\.)? # separator
    \d{3} # first 3 digits
    (\s|-|\.) # separator
    \d{4} # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})? # extension
    )''', re.VERBOSE)

# Combining re.IGNORECASE, re.DOTALL, and re.VERBOSE

# If you want some regex to match case-insensitive, match newlines, and be in verbose mode, you can combine the arguments with the | operator

some_regex_value = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)

# Project: Phone Number and Email Address Extractor

# See phone_and_email.py for the project

# Summary:

    # Regular expressions are a powerful tool for matching text patterns
    # The re.compile() function returns Regex objects
    # Regex objects have a search() method that searches the string it is passed for any matches to the regex
    # The search() method will return None if no text is found
    # Regex objects have a findall() method that will return all matches in a list
    # Regex objects have search() and findall() methods that will return Match objects
    # Match objects have group() method that will return the actual matched text