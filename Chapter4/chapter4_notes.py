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

# the
supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])


