from count_inv import *
import os

def line_to_lst(path):
    """
    takes path, reads each line in file and converts to int, assumes lines are
    integers already
    """
    with open(path, mode='r') as a_file:
        num_lst = []
        for line in a_file:
            num_lst.append(int(line))
    #print(num_lst)                                                             needed to have this print as was forgetting to convert lines from file (default str) into integers so inversions were wrong
    return num_lst


def run():
    """
    runs prompts and executes count inversions on entered text file
    """
    print("Home directory being used: " + os.path.expanduser('~'))              #expanduser('~') in Unix this is shorthand for home directory, unsure if this notation works in Windows - need to test
    folders = []

    while True:
        val = input("Enter folder names and file name with extension, if no more"
            "\nthen type 'no more': ")
        if val.lower() == 'no more':
            break
        folders.append(val)
    path = os.path.join(os.path.expanduser('~'),*folders)                       # "splat" operator * put before the iterable object folders in order to unpack list arguments into proper join() method arg values

    print("Count Inversions from this file:\n" + path)

    _ = input("Continue? (Y/N):")

    if _.lower() == "y":
        print("Running...")
        lst = line_to_lst(path)
        print("Read file, now counting inversions...")
        result = count_inversions(lst)[1]
        print("# of inversions in file: " + str(result))

    else:
        print("Aborted")

run()
