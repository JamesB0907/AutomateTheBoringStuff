# Functions:

# first example found in hello_func.py

# def Statements with Parameters:

# example in hello_func2.py

# Define, Call, Pass, Argument, Parameter:

    # Define: to create a function
    # Call: to execute a function
    # Pass: to give a function an argument
    # Argument: the value passed to the function
    # Parameter: the variable that stores the argument

# Return Values and Return Statements:

# when creating a function using the def statement, you can specify what the return value should be using the return statement using:
    # the return keyword
    # the value or expression that the function should return

# example in magic_8_ball.py

# The None Value:

# None is a special value that represents the absence of a value. It is the only value of the NoneType data type.

spam = print('Hello!')
# -> Hello!
None == spam
# -> True

# similar to a static void method in C#, it doesn't return anything, which, if no return is specified, the function will return None (invisibly).

# Keyword Arguments and print() Function:

# the print() function has two optional keyword arguments:
    # sep - the separator between arguments (default is a space)
    # end - the character that comes at the end of the string (default is a newline)

# sep:
print('Hello', 'World', sep='*')
# -> Hello*World

print('cats', 'dogs', 'mice', sep=',')
# -> cats,dogs,mice

# end:
print('Hello', end='')
print('World')
# -> HelloWorld

# The Call Stack:

# the call stack is a way to keep track of where the program is in a function. When a function is called, the program jumps to that function and executes it, then returns to where it left off.

# see abc_call_stack.py for an illustration of the call stack

# Local and Global Scope:

# local scope - variables that are created inside a function are local to that function and cannot be accessed outside of it

# global scope - variables that are created outside of a function are global and can be accessed anywhere in the program

def scope_spam():
    eggs = 31337
scope_spam()
# print(eggs)
# -> NameError: name 'eggs' is not defined

def local_spam():
    eggs = 99
    bacon()
    print(eggs)
def bacon():
    hame = 101
    eggs = 0
local_spam()
# -> 99

def global_spam():
    print(eggs2)
eggs2 = 42
global_spam()
print(eggs2)
# -> 42

def another_spam():
    eggs3 = 'spam local'
    print(eggs3) # prints 'spam local'
def bacon2():
    eggs3 = 'bacon local'
    print(eggs3) # prints 'bacon local'
    another_spam()
    print(eggs3) # prints 'bacon local'
eggs3 = 'global'
bacon2()
print(eggs3) # prints 'global'

# The Global Statement:

# using the global statement allows you to modify a global variable from within a function

def spam_with_global_eggs():
    global eggs
    eggs = 'spam'
eggs = 'global'
spam_with_global_eggs()
print(eggs) # -> spam

# refer to same_name_local_global.py for an example of local and global variables with the same name

# Exception Handling:

# def exception_spam(divide_by):
#     return 42 / divide_by
# print(exception_spam(2))
# print(exception_spam(12))
# print(exception_spam(0))
# print(exception_spam(1))

# cannot divide by 0, so the program will throw an error

# try and except Statements:

def exception_spam2(divide_by):
    try:
        return 42 / divide_by
    except ZeroDivisionError:
        print('Error: Invalid argument.')
print(exception_spam2(2))
print(exception_spam2(12))
print(exception_spam2(0))
print(exception_spam2(1))


