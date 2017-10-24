#!/usr/local/bin/python3
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
        parser.add_argument("N", type=int, nargs='?', default=10,
                            help="The number of extensions to generate.")
        return parser.parse_args()

    args = parse_args()
    for exttype in range(args.N):
        for ext in range(exttype):
            touch('./test/file{}.ext{}'.format(ext, exttype), ext*exttype)

    print('Done.')
