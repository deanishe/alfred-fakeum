#!/usr/bin/env python
# encoding: utf-8
#
# Copyright © 2014 deanishe@deanishe.net
#
# MIT Licence. See http://opensource.org/licenses/MIT
#
# Created on 2014-12-29
#

"""
"""

from __future__ import print_function, unicode_literals, absolute_import

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__)),
                'src'))

from workflow import Workflow

import fakum


def main():
    wf = Workflow()
    fakum.wf = wf
    print('| Name | Example |')
    print('|-- |--|')
    for name in fakum.FAKERS:
        ex = fakum.get_fake_datum(name)
        print('| {} | {} |'.format(name, ex).encode('utf-8'))


if __name__ == '__main__':
    sys.exit(main())
