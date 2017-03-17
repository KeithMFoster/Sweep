# Sweep
Python Directory Sweep for aged files

If you are like me, and your scripts and programs create a boat ton of log files, there are times that files need to be purged. This scritp file was designed to delete the files that are contained in a list of directories and are older than seven days.

Sounds a little mudain, but a little housekeeping goes a long ways.

To set up, put the full qualified directory path in the list, as the example below:

directory_list = [
    "C:\Program Files (x86)\RedRocket\myDirectory\Logs",
    "C:\Program Files (x86)\RedRocket\AnimalWorld\Logs"
]

Call the routine:
> python sweep.py


