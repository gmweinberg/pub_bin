#!/bin/bash

MYIP=`curl ifcfg.me`
TODAY=`date -I`
echo "$TODAY  $MYIP"

