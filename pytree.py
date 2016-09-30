#!/usr/bin/env python3
import subprocess
import sys
import os
#Aftering googling, I know that there is a python built-in function named os.walk to
#help me generate the file names in a directory tree by walking the tree either top-down or bottom-up
#it yields a 3-tuple (dirpath, dirnames, filenames)
#dirpath is a string, the path to the directory. dirnames is a list of the names of the subdirectories in dirpath.
#filenames is a list of the names of the non-directory files in dirpath.
#So, we need to delete the 'path' part in the root string to get the tree structure

if len(sys.argv)==2:
    path = sys.argv[1]
    for root, dirs, files in os.walk(path):
    #After geting 'root', we need to know the level of each root(how many subdirectories it has), which means we
    #need to calculate the number of '/' in each root.
        level = root.replace(path, '').count(os.sep)
        indent = ' ' * 2 
        symbol = '|'
        indent = symbol+indent
        indent = indent * (level)
        #indent = '|{}'.format(indent)
        print('{}|--{}'.format(indent, os.path.basename(root)))
        subindent = ' ' * 2
        subindent = symbol+subindent
        subindent = subindent * (level)
        #subindent = '{}'.format(subindent)
        for f in files:
            print('{}|-- {}'.format(subindent, f))
elif len(sys.argv)==1:
    path = os.getcwd()
else:
    print('Invalid Input')
if __name__ == '__main__':
    # just for demo
    subprocess.run(['tree'] + sys.argv[1:])
