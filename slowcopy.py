#!/usr/bin/env python
"""Form command line enter a target directory name. Create a subdir of the current directory with
the same name and copy all files into the new directory."""
# I find this uis necessary to get my car stereo to play files off a usb stick in the correct order
import sys, time
from os import listdir
import pathlib

if __name__ == '__main__':
    current = pathlib.Path().absolute()
    print('current', current)
    target = sys.argv[1]
    path = pathlib.Path(target)
    print('target dir name', path.name)
    # os.mkdir(path.name)
    for afile in listdir(target):
        srcfile = target + '/' + afile
        destfile = str(current) + '/' + str(path.name) + '/' + afile
        print(srcfile, destfile)
        time.sleep(2)
    
