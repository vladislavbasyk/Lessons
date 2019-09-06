#!/usr/bin/env python3
while True:
	s=input('Enter the: ')
	if s=='end':
		break
	if len(s)<3:
		print('too few')
		continue
	print('sufficient string length')
