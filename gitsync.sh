#!/bin/bash
# go through a list of dirs and git pull them
#
while read p; do
		if [ -d "$p" ]; then
		     echo "$p exists"
		fi
done <~/pub_include/.gitsync
