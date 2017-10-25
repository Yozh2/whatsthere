#!/usr/local/bin/python3

"""
extmaker - testfiles generator. Use it to quickly create N fileX.extX files with different sizes. Note that each extN has only N files (file0.extN ... fileN-1.extN)
"""

import argparse
import os

def touch(path='.', file_id=0):
    basedir = os.path.dirname(path)
    if not os.path.exists(basedir):
        os.makedirs(basedir)
    with open(path, 'w') as tempfile:
        os.utime(path, None)
        for byte in range(file_id):
            tempfile.write(str(byte))

if __name__=='__main__':

    def parse_args():
        """ Parses arguments and returns args object to the main program"""
        parser = argparse.ArgumentParser()
        parser.add_argument("PATH", type=str, nargs='?', default='.',
                            help="The path to the directory we want to generate files in.")
        parser.add_argument("N", type=int, nargs='?', default=10,
                            help="The number of extensions to generate.")
        return parser.parse_args()

    args = parse_args()
    for exttype in range(args.N):
        for ext in range(exttype):
            file_path = os.path.join(args.PATH, 'file{}.ext{}'.format(ext, exttype))
            touch(file_path, ext*exttype)

    print('Done.')
