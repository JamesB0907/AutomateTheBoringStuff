# Automate the Boring Stuff Chapter 9 Notes

# Files and File Paths:

# A file has two key properties: a filename (usually written as one word) and a path. The path specifies the location of a file on the computer. Here are some examples of file paths:

# Backslash on Windows and Forward Slash on macOS and Linux:

# Windows uses backslashes (\) as the separator between folder names in a file path, while macOS and Linux use forward slashes (/). If you want your programs to work on all operating systems, you will have to write your Python scripts to handle both cases.

# The path() function in the os module will return a string of the path with the appropriate file path separators.

# Using the / Operator to Join Paths:

# You can use the / operator similar to the + operator to join paths together. This will make your scripts more readable and work on all operating systems.

# You can even join two separate iterations of Path() together with the / operator.

# It is not recommended to concatenate the \ character with + to join paths together. This is because the \ character will only work on Windows, and not on macOS or Linux.

# One of the first two values passed to the Path() function must be a Path object.

# The Current Working Directory:

# The current working directory is the folder that any relative paths are relative to. You can get the current working directory as a string value with the os.getcwd() function and change it with os.chdir().

# The Home Directory:

# The home directory is the folder that contains all of the user's files. You can get the home directory as a string value with the os.path.expanduser('~') function.

# Absolute vs. Relative Paths:

# Absolute Paths start at the root and include the entire path to the file

# Relative Paths start from the current working directory

# Creating New Folders Using the os.makedirs() Function:

# You can create new folders with the os.makedirs() function. You can also create multiple folders at once by separating the folder names with the os.path.sep character.

# The os.makedirs() function will create all the intermediate folders if they do not exist.

# .mkdir() will only create the last folder in the path.

# Handling Absolute and Relative Paths:

# is_absolute() will return True if the path is an absolute path and False if it is a relative path.

# Using Path.cwd() will return the current working directory as a Path object.

# You can even use this to splice your current absolute path with a new relative path.

# Other useful function of the os.path module:

    # os.path.abspath() will return a string of the absolute path of the argument.
    # os.path.isabs() will return True if the argument is an absolute path and False if it is a relative path.
    # os.path.relpath() will return a string of a relative path from the start path to the end path.

# Getting the Parts of a File Path:

# Given a Path object, you can extract the file path's different parts with several attributes:

    # .drive will return the drive letter or root folder of the path.
    # .root will return the root folder of the path.
    # .anchor will return the concatenation of the drive and root.
    # .parents will return a sequence of the path's ancestors.
    # .name will return the file or folder name at the end of the path.
    # .stem will return the file name without the suffix.
    # .suffix will return the file name's extension.
    # .anchor will return the concatenation of the drive and root.

# .parents can be indexed to get the parent folder of the path.

# Path.cwd().parents[0] will return the parent folder of the current working directory.
    # ie: Something like Path.cwd().parents[6] will retrn a parent folder six levels up from the current working directory.

# os.path.basename() will return the file name and extension of the argument.

# os.path.split() will return a tuple of the argument's directory and file name.
    # ie: os.path.split('C:\\Users\\Al\\Documents\\example.txt') will return ('C:\\Users\\Al\\Documents', 'example.txt')

# (*i still don't understand the difference between a tuple and a list)

# os.path.dirname() will return the directory part of the argument.
    # ie: os.path.dirname('C:\\Users\\Al\\Documents\\example.txt') will return 'C:\\Users\\Al\\Documents'

# Finding File Sizes and Folder Contents:

# os.path.getsize() will return the size of the file in bytes.
# os.listdir() will return a list of strings of filenames in the argument's directory.

import os
from pathlib import Path, WindowsPath

total_size = 0
for filename in os.listdir('C:\\Windows\\System32'):
    total_size = total_size + os.path.getsize(os.path.join('C:\\Windows\\System32', filename))
print(str(round(total_size / 1e+9, 2)) + ' GB')

# Modifying a List of Files Using Glob Patterns:

# The glob module provides a function for making file lists from directory wildcard searches.

p = Path('C:/Users/Al/Documents')
p.glob('*')
# <generator object Path.glob at 0x0000021D3D3D3F90>
list(p.glob('*')) # Returns a list from the generator.
[WindowsPath('C:/Users/Al/Desktop/1.png'), WindowsPath('C:/Users/Al/Desktop/2.png'), WindowsPath('C:/Users/Al/Desktop/3.png'),
# ---snip---
WindowsPath('C:/Users/Al/Desktop/zzz.txt')]

# * return all files in the directory

# You can also use complex expressions:

list(p.glob('*.txt')) # List all files with .txt extension

# The ? character will match any single character:

list(p.glob('project?.docx'))
[WindowsPath('C:/Users/Al/Documents/project1.docx'), WindowsPath('C:/Users/Al/Documents/project2.docx')] # etc...

# You can combine the * and ? characters to match multiple characters:

list(p.glob('*.?x?'))
[WindowsPath('C:/Users/Al/Desktop/calc.exe'), WindowsPath('C:/Users/Al/Desktop/notes.txt'), WindowsPath('C:/Users/Al/Desktop/zzz.txt')]

# Creating a loop with the glob() method:
p = Path('C:/Users/Al/Desktop')
for textFilePathObj in p.glob('*.txt'):
    print(textFilePathObj) # Prints the Path object as a string.
    # Do something with the text file.

# C:/Users/Al/Desktop/foo.txt
# C:/Users/Al/Desktop/spam.txt
# C:/Users/Al/Desktop/zzz.txt

# Checking Path Validity:

    # os.path.exists() will return True if the file or folder exists.
    # os.path.isfile() will return True if the argument is a file.
    # os.path.isdir() will return True if the argument is a folder.

win_dir = Path('C:/Windows')
not_exists_dir = Path('C:/ThisFolderDoesNotExist')
calc_file = Path('C:/Windows/System32/calc.exe')
win_dir.exists()
# True
win_dir.is_dir()
# True
not_exists_dir.exists()
# False
calc_file.exists()
# True
calc_file.is_file()
# True

# These methods can be used to check if a file or folder exists before opening it.

# You can also determine things like if a drive is DVD or Flash Drive is attached:

d_drive = Path('D:/')
d_drive.exists()
# False

# The File Reading/Writing Process:

# Python allows you the ability to read certain files with simple methods

# Binary files are scrambled text files that are not human readable. They are used for things like images, videos, and executables.

# The write_text() method will write a string to a file.

from pathlib import Path
p = Path('C:/Users/Al/Desktop/hello.txt')
p.write_text('Hello, world!')
# 13
p.read_text
# 'Hello, world!'

# These Path objects only allow limited interactions:

    # open() function returns a file object
    # read() method reads the file
    # write() method writes to the file

# These are very similar to terminal commands (like SHELL or BASH)

# Opening Files with the open() Function:

# The open() function will return a file object that can be used to read or write to the file.

hello_file = open(Path.home() / 'hello.txt')

# It can also accept strings:
hello_file = open('C:\\Users\\your_home_folder\\hello.txt')

# MacOS version:
hello_file = open('/Users/your_home_folder/hello.txt')


