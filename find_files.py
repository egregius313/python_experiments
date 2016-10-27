#!/usr/bin/env python

import os


def find(pattern):
    for root, dirs, files in os.walk('/'):
        for dir in dirs:
            if pattern.lower() in dir.lower():
                print(os.path.join(root, dir))
        for file in files:
            if pattern.lower() in file.lower():
                print(os.path.join(root, file))


if __name__ == '__main__':
    print('Enter !q to quit')
    while True:
        pattern = input('Pattern: ')
        if pattern.startswith('!q'):
            break
        find(pattern)
