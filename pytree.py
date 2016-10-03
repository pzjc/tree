#!/usr/bin/env python3
import subprocess
import sys
import os
num_dirs = 0
num_files = 0


def tree(r, level):


    global num_dirs
    global num_files
    lst1 = os.listdir(r)
    i = 0
    lst2 = []
    for item in os.listdir(r):
        if not item.startswith('.'):
            lst2.append(item)
    for item in sorted(lst2, key=str.lower):
            i = i + 1
            if os.path.isdir(r + '/' + item):
                num_dirs = num_dirs + 1
                if i == len(lst2):
                    print('{}`-- {}'.format(level, item))
                    tree((r + '/' + item),level + '    ')
                else:
                    print('{}|-- {}'.format(level, item))
                    tree((r + '/' + item),level+'|   ')
            else:
                num_files = num_files + 1
                if i == len(lst2):
                    print('{}`-- {}'.format(level, item))
                else:
                    print('{}|-- {}'.format(level, item))
if __name__ == '__main__':
#    subprocess.run(['tree'] + sys.argv[1:])
    if len(sys.argv) == 2:
        path = sys.argv[1]
        print  (path)
        tree(path, '')
        print  (num_dirs, 'directories,', num_files, 'files')
    elif len(sys.argv) == 1:
        path = os.getcwd()
        print  ('.')
        tree(path, '')
        print  (num_dirs, 'directories,', num_files, 'files')
    else:
        print  ('Invalid Input!')
