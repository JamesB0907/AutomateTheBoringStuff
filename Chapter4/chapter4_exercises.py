# 1. What is []?

# An empty list.

# 2. How would you assign the value 'hello' as the third value in a list stored in a variable named spam? (Assume spam contains [2, 4, 6, 8, 10].)

# spam[2] = 'hello'

# For the following three questions, let’s say spam contains the list ['a', 'b', 'c', 'd'].

# 3. What does spam[int(int('3' * 2) // 11)] evaluate to?

# d because int('3' * 2) is 33 and 33 // 11 is 3, which is the index of d.

# 4. What does spam[-1] evaluate to?

# d because -1 is the last index of the list.

# 5. What does spam[:2] evaluate to?

# ['a', 'b'] because 2 is not included in the slice.

# For the following three questions, let’s say bacon contains the list [3.14, 'cat', 11, 'cat', True].

# 6. What does bacon.index('cat') evaluate to?

# 1 because 'cat' is at index 1.

# 7. What does bacon.append(99) make the list value in bacon look like?

# [3.14, 'cat', 11, 'cat', True, 99]

# 8. What does bacon.remove('cat') make the list value in bacon look like?

# [3.14, 11, 'cat', True]

# 9. What are the operators for list concatenation and list replication?

# The operator for list concatenation is + and the operator for list replication is *.

# 10. What is the difference between the append() and insert() list methods?

# append() adds a value to the end of a list and insert() adds a value to a specific index in a list.

# 11. What are two ways to remove values from a list?

# The del statement and the remove() list method. The del statement can remove a value at a specific index and the remove() list method can remove a specific value.

# 12. Name a few ways that list values are similar to string values.

# strings can be iterated over with a for loop and so can lists, strings can be sliced and so can lists, strings can be concatenated and so can lists, strings can be replicated and so can lists.

# 13. What is the difference between lists and tuples?

# Lists are mutable and tuples are immutable.

# 14. How do you type the tuple value that has just the integer value 42 in it?

# (42,)

# 15. How can you get the tuple form of a list value? How can you get the list form of a tuple value?

# tuple([1, 2, 3]) and list((1, 2, 3))

# 16. Variables that “contain” list values don’t actually contain lists directly. What do they contain instead?

# They contain references to the list values.

# 17. What is the difference between copy.copy() and copy.deepcopy()?

# copy.copy() makes a shallow copy of a list and copy.deepcopy() makes a copy of a list and all of its nested lists.

# Practice Projects:

# Comma Code:

spam = ['apples', 'bananas', 'tofu', 'cats']

def comma_code(list):
    for i in list:
        if i != list[-1]:
            print(i + ', ', end='')
        else:
            print('and ' + i)

comma_code(spam)

# Coin Flip Streaks:

# see coin_flip_streaks.py

