# Regex Search:

import re

re_search = open('regex_search.py', 'r')
re_search_text = re_search.read()
re_search.close()

print('Enter a regular expression:')
user_regex = input()
re_search_regex = re.compile(user_regex)
re_search_matches = re_search_regex.findall(re_search_text)

for match in re_search_matches:
    print(match)
