#!/bin/bash
THEN=`expr $(date +%s) - 86400 "*" $1`
#echo $THEN
echo `date -d @$THEN --rfc-3339=date`
