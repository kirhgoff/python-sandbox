#!/usr/bin/env python

from zipfile import ZipFile

import file_traverse
import sys

from tools.csvdump import CsvData


def process_zip_file(filepath):
    #print 'processing', filepath
    # try to read it as zip and close right away
    arch = ZipFile(filepath, 'r')
    for entry in arch.infolist():
        if 'com.moex.eif.model.eq.EqSecurity.csv' in entry.filename:
            process_file(arch.open(entry))
    arch.close()

def process_file(csvfile): 
    sec2faceUnit = {}
    securities = CsvData(csvfile, 'EqSecurity')
    for s in securities:
        if s.secCode in sec2faceUnit:
            if  sec2faceUnit[s.secCode]!=s.faceUnit:
                print '!!!!!!', s.secCode,sec2faceUnit[s.secCode],s.faceUnit,s.secBoard,csvfile
        else:
            sec2faceUnit[s.secCode] = s.faceUnit

if __name__ == '__main__':
    for filepath in sys.argv[1:]:
        file_traverse.process_dir_path(filepath, process_zip_file)

