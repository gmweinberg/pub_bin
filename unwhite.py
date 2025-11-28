#!/usr/bin/env python3
import sys

if len(sys.argv) < 2:
    print("Usage: script.py <file1> [file2] ...")
    sys.exit(1)

for filename in sys.argv[1:]:
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
        
        # Remove trailing whitespace from each line
        lines = [line.rstrip() + '\n' for line in lines]
        
        # Remove trailing blank lines
        while lines and lines[-1].strip() == '':
            lines.pop()
        
        # Write back
        with open(filename, 'w') as f:
            f.writelines(lines)
        
        print(f"Cleaned: {filename}")
    except Exception as e:
        print(f"Error processing {filename}: {e}")