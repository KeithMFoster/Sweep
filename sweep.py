
import os
import time

now = time.time()

# How many days back do we expire the files? lets set it seven.
ExpireDays = now - (7 * 86400)


# List of the directories to search for files that exceed the expiration period. Place the
# files in the list with its full path to the directory.
directory_list = [
    "C:\Program Files (x86)\RedRocket\myDirectory\Logs",
    "C:\Program Files (x86)\RedRocket\AnimalWorld\Logs"
]

for myDirectories in directory_list:
    try:
        files = os.listdir(myDirectories)
        for myFiles in files:
            if os.path.isfile(myDirectories + chr(92) + myFiles):
                t = os.stat(myDirectories + chr(92) + myFiles)
                if t.st_ctime < ExpireDays:
                    print("Deleting => " + myDirectories + chr(92) + myFiles)
                    os.remove(myDirectories + chr(92) + myFiles)
    except:
        print("Cannot access : " + myDirectories)
