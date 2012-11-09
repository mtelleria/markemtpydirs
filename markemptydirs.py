#!/usr/bin/python
# -*- coding: utf-8 -*-

# Inspired by https://git.wiki.kernel.org/index.php/MarkEmptyDirs

import sys
import os
import argparse
import shutil

class opt:
    file = ""
    text = ""
    filename = '.gitignore'
    
def main():

    parse_argv()

    # We do an os.walk to detect empty dirs
    list_of_emptydirs = []
    for (dirpath, dirnames, filenames) in os.walk('.'):
        if not dirnames and not filenames:
            list_of_emptydirs.append(dirpath)

#    print "empty dirs: %s " % list_of_emptydirs

    for emptydir in list_of_emptydirs:
        if opt.file:
            shutil.copyfile(opt.file, emptydir)
        else :
            with open(emptydir + '/' + opt.filename, 'w') as myfile:
                if opt.text:
                    myfile.write(opt.text + '\n')

    print "Marked %d directories" % len(list_of_emptydirs)

    
def parse_argv() :

    parser = argparse.ArgumentParser(description='create empty or template files in empty directories')

    parser.add_argument('--file',
                        help = 'Template file to copy to every empty directory')

    parser.add_argument('--text',
                        help = 'Text to place in the empty file')

    parser.add_argument('--filename',
                        default = opt.filename,
                        help = 'Filename to use (default .gitignore)')

    args = parser.parse_args()

    opt.file = args.file
    opt.text = args.text
    opt.filename = args.filename

if __name__ == '__main__':
    main()
