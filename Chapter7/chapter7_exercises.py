# Automate the Boring Stuff Chapter 7 Exercises
import re
# Practice Questions:

# 1. What is the function that creates Regex objects?

# re.compile()

# 2. Why are raw strings often used when creating Regex objects?

# Raw strings are used so that the backslashes are not interpreted as escape characters.

# 3. What does the search() method return?

# It returns the first group that satisfies the regex pattern.

# 4. How do you get the actual strings that match the pattern from a Match object?

# By calling the group() method on the Match object.

# 5. In the regex created from r'(\d\d\d)-(\d\d\d-\d\d\d\d)', what does group 0 cover? Group 1? Group 2?

# Group 0 covers the entire match, group 1 covers the first set of parentheses, and group 2 covers the second set of parentheses.

# 6. Parentheses and periods have specific meanings in regular expression syntax. How would you specify that you want a regex to match actual parentheses and period characters?

# By using a backslash before the parentheses and period characters.

# 7. The findall() method returns a list of strings or a list of tuples of strings. What makes it return one or the other?

# If the regex has no groups, findall() will return a list of strings. If the regex has groups, findall() will return a list of tuples of strings.

# 8. What does the | character signify in regular expressions?

# The | character signifies an OR statement in regular expressions.

# 9. What two things does the ? character signify in regular expressions?

# The ? character can signify an optional group or a nongreedy match.

# 10. What is the difference between the + and * characters in regular expressions?

# The + character matches one or more of the preceding group, while the * character matches zero or more of the preceding group.

# 11. What is the difference between {3} and {3,5} in regular expressions?

# {3} will match exactly 3 of the preceding group, while {3,5} will match between 3 and 5 of the preceding group.

# 12. What do the \d, \w, and \s shorthand character classes signify in regular expressions?

# \d signifies any numeric digit from 0 to 9, \w signifies any letter, numeric digit, or the underscore character, and \s signifies any space, tab, or newline character.

# 13. What do the \D, \W, and \S shorthand character classes signify in regular expressions?

# \D signifies any character that is not a numeric digit from 0 to 9, \W signifies any character that is not a letter, numeric digit, or the underscore character, and \S signifies any character that is not a space, tab, or newline character.

# 14. What is the difference between .* and .*?

# .* will match any character except for a newline, while .*? will match any character including a newline.

# 15. What is the character class syntax to match all numbers and lowercase letters?

# [0-9a-z]

# 16. How do you make a regular expression case-insensitive?

# By passing re.IGNORECASE as the second argument to re.compile().

# 17. What does the . character normally match? What does it match if re.DOTALL is passed as the second argument to re.compile()?

# The . character normally matches any character except for a newline. If re.DOTALL is passed as the second argument to re.compile(), the . character will match any character including a newline.

# 18. If numRegex = re.compile(r'\d+'), what will numRegex.sub('X', '12 drummers, 11 pipers, five rings, 3 hens') return?

# 'X drummers, X pipers, five rings, X hens'

# 19. What does passing re.VERBOSE as the second argument to re.compile() allow you to do?

# It allows you to add whitespace and comments to the regex string to make it more readable.

# 20. How would you write a regex that matches a number with commas for every three digits? It must match the following:

# '42'
# '1,234'
# '6,368,745'
# but not the following:
# '12,34,567' (which has only two digits between the commas)
# '1234' (which lacks commas)

re.compile(r'^\d{1,3}(,\d{3})*$')

# 21. How would you write a regex that matches the full name of someone whose last name is Watanabe? You can assume that the first name that comes before it will always be one word that begins with a capital letter. The regex must match the following:

# 'Haruto Watanabe'
# 'Alice Watanabe'
# 'RoboCop Watanabe'

# but not the following:
# 'haruto Watanabe' (where the first name is not capitalized)
# 'Mr. Watanabe' (where the preceding word has a nonletter character)
# 'Watanabe' (which has no first name)

re.compile(r'[A-Z][a-z]*\sWatanabe')

# 22. How would you write a regex that matches a sentence where the first word is either Alice, Bob, or Carol; the second word is either eats, pets, or throws; the third word is apples, cats, or baseballs; and the sentence ends with a period? This regex should be case-insensitive. It must match the following:

# 'Alice eats apples.'
# 'Bob pets cats.'
# 'Carol throws baseballs.'
# 'Alice throws Apples.'
# 'BOB EATS CATS.'

# but not the following:
# 'RoboCop eats apples.'
# 'ALICE THROWS FOOTBALLS.'
# 'Carol eats 7 cats.'

re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.', re.IGNORECASE)

# Practice Projects:

# Date Detection:

re.compile(r'''(
    (0[1-9]|[12]\d|3[01])/ # day
    (0[1-9]|1[0-2])/ # month
    ([12]\d{3}) # year
    )''', re.VERBOSE)

# Strong Password Detection:

re.compile(r'''(
    ^(?=.*[A-Z].*[A-Z]) # at least two capital letters
    (?=.*[!@#$&*]) # at least one of these special characters
    (?=.*[0-9].*[0-9]) # at least two numeric digits
    (?=.*[a-z].*[a-z].*[a-z]) # at least three lower case letters
    .{8,} # at least 8 characters long
    $ # end-of-string
    )''', re.VERBOSE)

# Regex Version of the strip() Method:

def strip_regex(string, char=None):
    if char is None:
        strip_regex = re.compile(r'^\s*|\s*$')
    else:
        strip_regex = re.compile(f'^[{char}]*|[{char}]*$')
    return strip_regex.sub('', string)
