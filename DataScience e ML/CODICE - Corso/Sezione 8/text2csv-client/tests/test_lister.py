#!/usr/bin/env python3

from os.path import join
import lister
from unittest import mock

posdir = "/example/positive"
negdir = "/example/negative"
lines = ["line 1", "line 2", "line 3"]
files = [join(posdir, "a.txt"), join(negdir, "b.txt")]


def test_lister():
    m = mock.mock_open(read_data="\n".join(lines))
    with mock.patch('glob.glob') as m_glob, \
            mock.patch("lister._readline") as m_readline:
        m_glob.return_value = files
        m_readline.return_value = [b"Some review text for testing"]

        for r in lister.lister(posdir, negdir):
            assert r != []
