# Automate the Boring Stuff Chapter 8 Exercises

# Practice Questions:

# 1. Does PyInputPlus come with the Python Standard Library?

# No

# 2. Why is PyInputPlus commonly imported with import pyinputplus as pyip?

# Shorter and easier to type

# 3. What is the difference between inputInt() and inputFloat()?

# inputInt() will only accept integer values, while inputFloat() will accept both integer and floating-point numbers.

# 4. How can you ensure that the user enters a whole number between 0 and 99 using PyInputPlus?

# You can use the inputInt() function with the min and max keyword arguments.

# 5. What is passed to the allowRegexes and blockRegexes keyword arguments?

# A list of regular expression strings that are either allowed or blocked from being entered.

# 6. What does inputStr(limit=3) do if blank input is entered three times?

# It will raise a RetryLimitException.

# 7. What does inputStr(limit=3, default='hello') do if blank input is entered three times?

# It will make the input function return the default value 'hello'.

# Practice Projects:

# Sandwich Maker:

# See sandwich_maker.py for the code.

# Write Your Own Multiplication Quiz:

import pyinputplus as pyip
import random, time

number_of_questions = 10
correct_answers = 0
for question_number in range(number_of_questions):
    # Pick two random numbers:
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    prompt = '#%s: %s x %s = ' % (question_number, num1, num2)
    try:
        # Right answers are handled by allowRegexes.
        # Wrong answers are handled by blockRegexes, with a custom message.
        pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)],
                      blockRegexes=[('.*', 'Incorrect!')],
                      timeout=8, limit=3)
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        # This block runs if no exceptions were raised in the try block.
        print('Correct!')
        correct_answers += 1

print('You got %s out of %s questions correct.' % (correct_answers, number_of_questions))

