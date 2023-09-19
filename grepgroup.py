#!/usr/bin/env python
"""Display grep capture group 1 if it exists"""
import sys, re

if __name__ == '__main__':
    pattern = re.compile(sys.argv[1])
    for line in sys.stdin:
         match = re.search(pattern, line)
         if match:
             print(match.group(1))

# cat sitemap.xml | grepgroup.py '<loc>([^<]+)'
