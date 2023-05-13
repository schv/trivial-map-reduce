#!/bin/python3

import os, sys
from pathlib import Path
import subprocess
from itertools import groupby
import tempfile

def main():
    assert len(sys.argv) == 5, f'Expected 4 arguments, got {len(sys.argv)}'
    
    name = sys.argv[0]
    operation = sys.argv[1].lower()
    assert operation in ('map', 'reduce'), \
        f'Unrecognized operation: {operation}, expected "map" or "reduce"'
    
    binary_path = Path(sys.argv[2])
    src_path    = Path(sys.argv[3])
    dst_path    = Path(sys.argv[4])

    with open(src_path) as src, open(dst_path, 'w') as dst:
        if operation == 'map':
            subprocess.run(sys.argv[2], stdin=src, stdout=dst)
        if operation == 'reduce':
            for key, group in groupby(sorted(src, key=lambda x: x[:x.find('\t')], reverse=True)):
                fd, path = tempfile.mkstemp()
                with open(path, 'w') as tmp:
                    tmp.writelines(group)
                subprocess.run(sys.argv[2], stdin=fd, stdout=dst)
                os.close(fd)
                

if __name__ == '__main__':
    main()
