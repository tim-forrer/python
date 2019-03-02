"""given a directory, scans for files of a given extension and ensures that they have no capital letters"""
import os

directory = ""
extension = ""

lst = os.listdir(directory)

for i in lst:
    lgth = len(i)
    if len(i) - len(extension) >= 0 and i[len(i) - len(extension):] == extension:
        os.rename(directory + "/" + i, directory + "/" + i.lower())

        