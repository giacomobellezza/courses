#!/usr/bin/env python3

from unittest import mock
import csv

from row import packer, output, fields


def test_csv_write():
    m = mock.mock_open()
    with mock.patch("builtins.open", m):
        with output("foo") as f:
            writer = csv.DictWriter(f, fieldnames=fields,
                                    quoting=csv.QUOTE_MINIMAL)
            writer.writeheader()

            r = packer("Hello, 世界", "positive")
            writer.writerow(r)
