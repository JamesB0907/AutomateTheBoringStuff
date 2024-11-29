# Automate the Boring Stuff Chapter 10 Exercises

# 1. What is the difference between the shutil.copy() function and the shutil.copytree() function?

# copy only words on one file while copytree copies all files in a folder

# 2. What function is used to rename files?

# move is used to rename files

# 3. What is the difference between the delete functions in the send2trash and shutil modules?

# send2trash sends files to the recycle bin while shutil deletes files permanently

# 4. ZipFile objects have a close() method just like File objects’ close() method. What ZipFile method is equivalent to File objects’ open() method?

# zipfile.ZipFile()

# Practic Projects:

# Selective Copy
import os, shutil

def selective_copy(folder, extension, destination):
    folder = os.path.abspath(folder)
    destination = os.path.abspath(destination)
    print(f'Copying files with the {extension} extension from {folder} to {destination}')
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            if filename.endswith(extension):
                print(f'Copying {filename}...')
                shutil.copy(os.path.join(foldername, filename), destination)


# Deleting Unneeded Files:

def delete_files(folder, size):
    folder = os.path.abspath(folder)
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            if os.path.getsize(os.path.join(foldername, filename)) > size:
                print(f'Deleting {filename}...')
                os.unlink(os.path.join(foldername, filename))

# Filling in the Gaps:

def fill_gaps(folder):
    folder = os.path.abspath(folder)
    files = os.listdir(folder)
    files.sort()
    for i, filename in enumerate(files):
        file_number = i + 1
        # zfill pads the number with zeros to ensure it is three digits long
        if filename.endswith(str(file_number).zfill(3)):
            continue
        new_filename = str(file_number).zfill(3) + os.path.splitext(filename)[1]
        print(f'Renaming {filename} to {new_filename}...')
        shutil.move(os.path.join(folder, filename), os.path.join(folder, new_filename))

# with regex instead of zfill:

def fill_gaps_regex(folder):
    folder = os.path.abspath(folder)
    files = os.listdir(folder)
    files.sort()
    for i, filename in enumerate(files):
        file_number = i + 1
        mo = re.search(r'\d+', filename)
        if mo == None:
            continue
        if int(mo.group()) == file_number:
            continue
        new_filename = re.sub(r'\d+', str(file_number), filename)
        print(f'Renaming {filename} to {new_filename}...')
        shutil.move(os.path.join(folder, filename), os.path.join(folder, new_filename))