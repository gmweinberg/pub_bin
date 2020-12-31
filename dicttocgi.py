#!/usr/bin/env python
"""Turn a stringified python dictionary into a cgi query string"""
import sys
from ast import literal_eval
from urllib.parse import quote

if __name__ == '__main__':
    myj = literal_eval(sys.argv[1])
    print('&'.join([quote(key) + '=' + quote(myj[key]) for key in myj]))
