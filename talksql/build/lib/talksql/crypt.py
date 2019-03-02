""" 
author - madhukumar seshadri
"""
import time
import uuid

__keys="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()_+=-`1234567890,./?'\";:\[{]}/"
__binkeys={}

for i,akey in enumerate(__keys):
	__binkeys[akey]=i

def binkey(key):
	if key in __binkeys:
		return __binkeys[key]
	else:
		return 2309999798797

def crypt(uval):
	now=time.localtime()
	mystify=str(uuid.uuid1())
	newval=""
	for i,v in enumerate(uval):
		newval += str(binkey(mystify[i]) * binkey(v))

	return (newval,mystify)

def check(incoming,stored1,stored2):
	output=False
	if not incoming: return output
	if not stored1: return output
	if not stored2: return output
	newval=""
	l = len(stored1)
	for i,v in enumerate(incoming):
		if i < l:
			newval += str(binkey(stored1[i]) * binkey(v))

	if newval == stored2:
		output=True

	return output

import sys
if __name__ == "__main__":
	a=sys.argv[1]
	b=sys.argv[2]
	x=crypt(a)
	print "result for",a,x 
	print check(b,x[1],x[0])
