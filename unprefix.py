#!/usr/bin/env python
"""Remove the prefix from the name for all files in the current directory"""
import os
import sys
import time

if __name__ == '__main__':
    prefix = '_'
    if len(sys.argv) > 1:
        prefix = ays.argv[1].strip()
    print("Removing through prefix {} from all files in current directory.".format(prefix))
    time.sleep(5)
    fid = os.listdir(".") #files in directory
    fid.sort()

    i = 1
    for afile in fid:
        index = afile.find(prefix)
        if index == -1:
            print("Prefix not found for file {}. Skipping".format(afile))
            time.sleep(5)
        else:
            new = afile[index + len(prefix):]
            print("Renaming {} to {}".format( afile, new))
            os.rename(afile, new)
