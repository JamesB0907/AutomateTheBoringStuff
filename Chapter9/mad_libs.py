# Mad Libs:

import re

mad_libs = open('mad_libs.txt', 'r')
mad_libs_text = mad_libs.read()
mad_libs.close()

mad_libs_regex = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')
mad_libs_matches = mad_libs_regex.findall(mad_libs_text)

for match in mad_libs_matches:
    if match == 'ADJECTIVE':
        print('Enter an adjective:')
    elif match == 'NOUN':
        print('Enter a noun:')
    elif match == 'ADVERB':
        print('Enter an adverb:')
    elif match == 'VERB':
        print('Enter a verb:')
    user_input = input()
    mad_libs_text = mad_libs_regex.sub(user_input, mad_libs_text, count=1)

mad_libs = open('mad_libs.txt', 'w')
mad_libs.write(mad_libs_text)
mad_libs.close()
print(mad_libs_text)

# Output:
# Enter an adjective:
# silly
# Enter a noun:
# dog
# Enter an adverb:
# quickly
# Enter a verb:
# ran
# The silly dog quickly ran to the store.