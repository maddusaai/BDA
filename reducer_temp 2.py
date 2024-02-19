#!/usr/bin/env python

import sys

current_year = None
total_temp = 0
count = 0
min_temp = float('inf')
max_temp = float('-inf')

for line in sys.stdin:
    line = line.strip()
    year, temp = line.split('\t')
    temp = float(temp)
    if current_year and current_year != year:
        avg_temp = total_temp / count
        print("{0},{1},{2},{3}".format(current_year, avg_temp, min_temp, max_temp))
        current_year = year
        total_temp = 0
        count = 0
        min_temp = float('inf')
        max_temp = float('-inf')
    current_year = year
    total_temp += temp
    count += 1
    min_temp = min(min_temp, temp)
    max_temp = max(max_temp, temp)

if current_year:
    avg_temp = total_temp / count
    print("{0},{1},{2},{3}".format(current_year, avg_temp, min_temp, max_temp))

