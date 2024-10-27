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


