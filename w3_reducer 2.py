#!/usr/bin/env python
import sys
 
current_unit = None
total_salary = 0
 
for line in sys.stdin:
    line = line.strip()
    unit, salary = line.split('\t', 1)
 
    try:
        salary = float(salary)
    except ValueError:
        continue
 
    if current_unit == unit:
        total_salary += salary
    else:
        if current_unit:
            print(f"{current_unit}\t\t{total_salary}")
        current_unit = unit
        total_salary = salary
 
# Output the last unit's total salary
if current_unit:
    print(f"{current_unit}\t{total_salary}")
