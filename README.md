# Sweep
Python Directory Sweep for aged files

If you are like me, your scripts and programs create a boat ton of log files. There are times that these files need to be purged or else they take over the hard drive. This script file was designed to delete the files contained in a preset list of directories, and older than seven days.

Sounds a little plain, but a little housekeeping goes a long ways.

To set up, put the full qualified directory path in the list, as the example below:

directory_list = [
    "C:\Program Files (x86)\RedRocket\myDirectory\Logs",
    "C:\Program Files (x86)\RedRocket\AnimalWorld\Logs"
]

Call the routine or better yet, put it in a cron for daily or weekly activation:
> python sweep.py


