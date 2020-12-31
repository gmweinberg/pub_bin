#!/usr/bin/env python
"""Turn a json/python dictionaly to a cgi query string"""
import sys
import json
from urllib.parse import quote

if __name__ == '__main__':
    myj = json.loads(sys.argv[1])
    print('&'.join([quote(key) + '=' + quote(myj[key]) for key in myj]))

        
    
    


