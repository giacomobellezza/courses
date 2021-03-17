#!/usr/bin/env python3

import glob
from os.path import join


def lister(positivedir, negativedir):
    files = glob.glob(join(positivedir, "*.txt"))
    files.extend(glob.glob(join(negativedir, "*.txt")))

    for f in files:
        for line in _readline(f):
            line = line.strip()
            if positivedir in f:
                yield [line, "positive"]
            else:
                yield [line, "negative"]


def _readline(filepath):
    with open(filepath, 'rb') as f:
        for line in f:
            yield line
