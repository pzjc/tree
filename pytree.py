#!/usr/bin/env python3
import subprocess
import sys
import os


if len(sys.argv) == 2:
    path = sys.argv[1]
    for root, dirs, files in os.walk(path):
        level = root.replace(path, '').count(os.sep)
        indent = ' ' * 2 
        symbol = '|'
        indent = symbol+indent
        indent = indent * (level)
        print('{}|--{}'.format(indent, os.path.basename(root)))
        subindent = ' ' * 2
        subindent = symbol+subindent
        subindent = subindent * (level)
        for f in files:
            print('{}|-- {}'.format(subindent, f))
elif len(sys.argv) == 1:
    path = os.getcwd()
else:
    print('Invalid Input')
if __name__ == '__main__':
    # just for demo
    subprocess.run(['tree'] + sys.argv[1:])
