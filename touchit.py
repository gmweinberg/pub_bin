#!/usr/bin/python
"""Update mod/access times for all file sin a tree."""
# My stupid-ass car usb player playes file in order of access time.
import sys
import os
import os.path
import time
from pathlib import Path


def touchem(apath):
    for afile in sorted(os.listdir(apath)):
        name = apath + '/' + afile
        print('checking {}'.format(name))
        if os.path.isdir(name):
            touchem(name)
        global when
        os.utime(name, (when, when))
        when += 60
        
if __name__ == '__main__':
    when = int(time.time()) - 3600 * 10
    theroot = '.'
    touchem(theroot)

