#!/usr/bin/env python3

from unittest import mock
from main import run

from test_lister import lines, posdir, negdir, files


def test_main():
    rowm = mock.mock_open()
    with mock.patch('glob.glob') as m_glob, \
            mock.patch('lister._readline') as m_readline, \
            mock.patch('builtins.open', rowm):

        m_glob.return_value = files
        m_readline.return_value = [b"Some review text for testing"]

        run(["--positivedir", posdir, "--negativedir", negdir])
