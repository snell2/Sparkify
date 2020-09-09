#!/usr/bin/python

import sys
import json
lst=[]
for line in sys.stdin:
    dic=line.split("\n")
    for d in dic:
        lst.append(d)

while("" in lst):
    lst.remove("")

for item in lst:
    s=json.loads(item)
    for val in s.values():
        print('%s\t%s'%(val,1))


