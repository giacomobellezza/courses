#!/usr/bin/env python3

import argparse
import csv
from os.path import expanduser
import row
import lister

desc = "Merge text files to one CSV file"

parser = argparse.ArgumentParser(description=desc)
parser.add_argument("--positivedir", required=True, type=str)
parser.add_argument("--negativedir", required=True, type=str)
parser.add_argument("--outputfile", type=str, default="output.csv")


def run(args=None):
    flags = parser.parse_args(args)

    with row.output(expanduser(flags.outputfile)) as f:
        csvw = csv.DictWriter(f, fieldnames=row.fields,
                              quoting=csv.QUOTE_MINIMAL)
        csvw.writeheader()

        for line in lister.lister(expanduser(flags.positivedir),
                                  expanduser(flags.negativedir)):
            r = row.packer(line[0], line[1])
            csvw.writerow(r)


if __name__ == "__main__":
    run(None)
