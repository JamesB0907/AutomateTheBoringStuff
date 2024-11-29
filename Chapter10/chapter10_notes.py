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

# Walking a Directory Tree:

# os.walk() is a generator that will yield three values on each iteration: the current folder name, a list of subfolders in the current folder, and a list of files in the current folder

for folder_name, subfolders, filenames in os.walk('C:\\delicious'):
    print('The current folder is ' + folder_name)
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folder_name + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folder_name + ': ' + filename)
    print('')

# Compressing Files with the zipfile Module:

# The zipfile module can be used to compress files into .zip archives or extract files from .zip archives

# Reading ZIP Files:

import zipfile, os
from pathlib import Path
p3 = Path.home()
example_zip = zipfile.ZipFile(p / 'example.zip')
example_zip.namelist()
# ['spam.txt', 'cats/', 'cats/catnames.txt', 'cats/zophie.jpg']
spam_info = example_zip.getinfo('spam.txt')
spam_info.file_size
# 13908
spam_info.compress_size
# 3828
print(f'Compressed file is {round(spam_info.file_size / spam_info.compress_size, 2)}x smaller!')
# Compressed file is 3.63x smaller!
example_zip.close()

# The above code opens a .zip file and prints the names of the files and folders inside it. It then gets the information about the spam.txt file and prints the size of the file and the size of the compressed file. Finally, it prints how much smaller the compressed file is compared to the original file.

# Extracting from ZIP Files:

import zipfile, os
from pathlib import Path
p4 = Path.home()
example_zip2 = zipfile.ZipFile(p / 'example.zip')
example_zip2.extractall()
example_zip2.extract('spam.txt')

# The extractall() method will extract all files and folders from the .zip file into the current working directory. The extract() method will extract a single file from the .zip file into the current working directory.

# Creating and Adding to ZIP Files:

import zipfile
new_zip = zipfile.ZipFile('new.zip', 'w')
new_zip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
new_zip.close()

# The above code creates a new .zip file and writes the spam.txt file to it. The compress_type argument specifies the compression algorithm to use. The ZIP_DEFLATED argument specifies the deflate compression algorithm, which works well on all types of data.

# Project: Renaming Files with American-Style Dates to European-Style Dates

# See code in rename_dates.py

# Project: Backing Up a Folder into a ZIP File

# See code in backup_to_zip.py

# Summary:

    # The shutil module provides functions for copying, moving, renaming, and deleting files.
    # The send2trash module sends files to the recycle bin or trash.
    # The zipfile module reads and writes ZIP files.
    # The os.walk() function walks a directory tree and returns filenames.
    # The os.unlink() function deletes a single file.
    # The os.rmdir() function deletes an empty folder.
    # The shutil.rmtree() function deletes a folder and all of its contents.

