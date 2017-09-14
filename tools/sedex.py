#!/usr/bin/env python

import fileinput
import re
 
for line in fileinput.input():
    line = re.sub(r'(([\sa-zA-Z0-9]+_)*\$\{today\.plusN\(\d,\'[yMd-]+\'\)\})',r'"\1"', line.rstrip())
    print(line)
