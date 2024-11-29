# Automate the Boring Stuff Chapter 10 Notes

# Organizing Files

# The shutil Module:

# The SHell UTILity module has functions to let you copy, move, rename, and delete files in your Python programs.

# Copying Files and Folders:

# The shutil.copy() function will copy a single file, while shutil.copytree() will copy an entire folder and every folder and file contained in it.

import shutil, os
from pathlib import Path
p = Path.home()
shutil.copy(p / 'spam.txt', p / 'some_folder')
# 'C:\\Users\\Al\\some_folder\\spam.txt'
shutil.copy(p / 'eggs.txt', p / 'some_folder/eggs2.txt')
# WindowsPath('C:/Users/Al/some_folder/eggs2.txt')

# shutil.copy() copies the file at the source path and pastes it at the destination path. If the destination path is a folder, the file will be copied into that folder. If the destination path is a file, the file will be copied and renamed to the destination path.

# shutil.copytree() will copy an entire folder and it's contents

p2 = Path.home()
shutil.copytree(p2 / 'spam', p2 / 'spam_backup')
# WindowsPath('C:/Users/Al/spam_backup')

# Moving and Renaming Files and Folders:

# shutil.move(source, destination) will move the file or folder to the destination

shutil.move('C:\\bacon.txt', 'C:\\eggs')
# 'C:\\eggs\\bacon.txt'

# The destination can also be a filename, which will rename the file or folder

shutil.move('C:\\bacon.txt', 'C:\\eggs\\new_bacon.txt')
# 'C:\\eggs\\new_bacon.txt'

# If both the source and destination are files, the source file will be renamed to the destination filename
shutil.move('C:\\bacon.txt', 'C:\\eggs')
# 'C:\\eggs

# Python will throw an exception if the destination folder does not exist

# Permanently Deleting Files and Folders:

    # os.unlink(path) will delete the file at the path
    # os.rmdir(path) will delete the folder at the path
    # shutil.rmtree(path) will delete the folder at the path and all of its contents

# Safe Deletes with the send2trash Module:

import send2trash
bacon_file = open('bacon.txt', 'a') # creates the file
bacon_file.write('Bacon is not a vegetable.')
# 25
bacon_file.close()
send2trash.send2trash('bacon.txt')