# 1. What are the two values of the Boolean data type? How do you write them?
# True and False

# 2. What are the three Boolean operators?
# and, or, not

# 3. Write out the truth tables of each Boolean operator (that is, every possible combination of Boolean values for the operator and what they evaluate to).
# and
    # True and True = True
    # True and False = False
    # False and True = False
    # False and False = False
# or
    # True or True = True
    # True or False = True
    # False or True = True
    # False or False = False
# not
    # not True = False
    # not False = True

# 4. What do the following expressions evaluate to?
    # (5 > 4) and (3 == 5) - False
    # not (5 > 4) - True
    # (5 > 4) or (3 == 5) - True
    # not ((5 > 4) or (3 == 5)) - False
    # (True and True) and (True == False) - False
    # (not False) or (not True) - True

# 5. What are the six comparison operators?
# > < >= <= == !=

# 6. What is the difference between the equal to operator and the assignment operator?
# The = is used to assign a value to an empty variable and == is used to compare two values and output a boolean value.

# 7. Explain what a condition is and where you would use one.
# A condition is a statement that is either true or false. You would use one in an if statement to determine the flow of the program.

# 8. Identify the three blocks in this code:
# spam = 0                block 1
# if spam == 10:          block 1
#     print('eggs')       block 2
#     if spam > 5:        block 2
#         print('bacon')  block 3
#     else:               block 2
#         print('ham')    block 3
#     print('spam')       block 2
# print('spam')           block 1

# 9. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.

spam = 0 
if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greetings!')

# 10. What keys can you press if your program is stuck in an infinite loop?
# CNTL + C

# 11. What is the difference between break and continue?
# break will take you out of the current loop and continue will go back to the beginning of the loop.

# 12. What is the difference between range(10), range(0, 10), and range(0, 10, 1) in a for loop?
# With one variable the range will be from 0 until that number, with two it will be between the two numbers, and with a third variable you can count by that third number.

# 13. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

for i in range(1, 11):
    print(i)

i = 1
while i < 11:
    print(i)
    i = i + 1

# 14. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?
# spam.bacon()

# Extra credit: Look up the round() and abs() functions on the internet, and find out what they do. Experiment with them in the interactive shell.

# round() rounds a number to the nearest whole number
print(round(5.5))
# -> 6

# abs() returns the absolute value of a number
print(abs(-5))
# -> 5
 

