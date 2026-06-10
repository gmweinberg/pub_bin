#!/bin/bash
TARGET=$1
sed -i 's/\t/\  /g' $TARGET
sed -i 's/\([^ ]\) \/\/ /\1  \/\/ /g' $TARGET
sed -i 's/){/) {/g' "$TARGET"
sed -i 's/while(/while (/g' "$TARGET"
sed -i 's/switch(/switch (/g' "$TARGET"

