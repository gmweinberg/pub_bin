#!/usr/bin/env python
# encoding: utf-8
import os
fid = os.listdir(".") #files in directory
fid.sort()

i = 1
for afile in fid:
    if i < 10:
        pre = "00" + str(i)
    elif i < 100:
        pre = "0" + str(i)
    else:
        pre = str(i)
    print(pre + afile)
    os.rename(afile, pre + afile)
    i = i + 1
