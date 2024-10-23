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



