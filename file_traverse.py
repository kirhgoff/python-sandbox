#!/usr/bin/env python

from glob import glob
import os.path


def process_dir_path(path, process_file_func):
    for filepath in expand_path(path):
        filepath = try_resolve_path(filepath)
        process_file_func(filepath)

def try_resolve_path(filepath):
    if os.path.isdir(filepath):
        return None
    elif os.path.isfile(filepath):
        return os.path.normpath(filepath)
    else:
        raise ValueError('Unknown file type '+filepath)

def expand_path(path):
    expanded  = []
    if '**' in path:
        if not ('/**/' in path or '\\**\\' in path):
            raise ValueError("Path may contain ** only in place of directory")
        if '**' in path.replace('**', '%%', 1):
            raise ValueError("Path may contain ** only once")
        # ugly but works
        for x in ['.','*','*/*','*/*/*','*/*/*/*','*/*/*/*/*','*/*/*/*/*/*','*/*/*/*/*/*/*']:
            expanded += glob(os.path.normpath(path.replace('**', x)))
    else:
        expanded += glob(os.path.normpath(path))
    return sorted(set(map(os.path.normpath, expanded)))


