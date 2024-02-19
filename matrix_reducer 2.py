#!/usr/bin/python3

import sys

a={}
b={}
for line in sys.stdin:
	line = line.strip()
	key,pos,value = line.split('\t')
	p = pos.split(',')
	if key=='a':
		a[(int(p[0]),int(p[1]))] = int(value)
	elif key=='b':
		b[(int(p[0]),int(p[1]))] = int(value)

add={}
sub={}
mul={}
result=0
print("Addition of two matrices is : \n")
for i in range(0,3):
	for j in range(0,3):
		add[(i,j)] = a[(i,j)]+b[(i,j)]
		sub[(i,j)] = a[(i,j)]-b[(i,j)]
		print ("{0}  ".format(add[(i,j)]))
print("Subtraction : \n")	
for i in range(0,3):
	for j in range(0,3):
		print("{0} ".format(sub[(i,j)]))
		for k in range(0,3):
			result=result+ a[(i,k)]*b[(k,j)]
		mul[(i,j)]= result
		result=0
print("Multiplication : \n")
for i in range(0,3):
        for j in range(0,3):
                print ("{0}  ".format(mul[(i,j)]))
print("Transpose of the product matrix : \n")
for i in range(0,3):
	for j in range(0,3):
		print(mul[(j,i)])

