#!/usr/bin/env python

import sys

for line in sys.stdin:
	line = line.strip()
	year,temperature = line.split('\t')
	print(f'{year}\t{temperature}')


