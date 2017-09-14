#!/usr/bin/env python

import sys

find = sys.argv[1]
replace = sys.argv[2]
fileList = sys.argv[3:]

#print "Processing files" + fileList

for filepath in fileList:
  with open(filepath) as f:
    s = f.read()
    s = s.replace(find, replace)
    try:
        with open(filepath, "w") as f:
            f.write(s) 
    except IOError:
        print ("Cannot write to %s" % filepath) 
