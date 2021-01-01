#!/usr/bin/env python
"""Turn a json dictionary (object) into a cgi query string"""
# comment
import sys
import json
from urllib.parse import quote

if __name__ == '__main__':
    myj = json.loads(sys.argv[1])
    print('&'.join([quote(key) + '=' + quote(myj[key]) for key in myj]))
