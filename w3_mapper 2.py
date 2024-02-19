#!/usr/bin/env python
import sys
 
for line in sys.stdin:
    line = line.strip()
    words = line.strip().split(',')
 
    # Ensure that the line has enough elements to extract unit and salary
    if len(words) >= 5:
        emp_no, emp_name, unit, designation, salary = words
        print(f"{unit}\t{salary}")
