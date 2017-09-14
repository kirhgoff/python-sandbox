'''
@author: sinyuginas
'''

import csv,re
from collections import namedtuple
import keyword

class CsvData:
    def __init__(self, csvfile, name = None):
        self.name = name
        if isinstance(csvfile, str):
            if not name:
                fname = re.split(r'\\|/',csvfile)[-1]
                self.name = sorted(fname.split('.'), key=len)[-1]
            csvfile = open(csvfile, 'r')
        if not self.name:
            raise ValueError('No type name given')
        csvreader = csv.reader(csvfile)
        self.header = csvreader.next()
        if 'sep=' in self.header: 
            self.header = csvreader.next()
        # avoid keywords
        field_names = map(lambda x : keyword.iskeyword(x) and x+"_" or x, self.header)
        self.dataclass = namedtuple(self.name, field_names)
        self.rows = []
        for row in csvreader:
            self.rows.append(self.dataclass(*row))
#         self.rows.sort()
        csvfile.close()

    def __iter__(self):
        return iter(self.rows)

    def __len__(self):
        return len(self.rows)

    def __getitem__(self, i):
        return self.rows[i]

    def __str__(self):
        return self.name +' '+ str(self.header)


