# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import os
from pkg_resources import resource_filename

_data_path = resource_filename(__name__, 'data.bin')
with open(_data_path, 'rb') as f:
    _replaces = f.read().decode('utf8').split('\x00')


def unidecode(txt):
    chars = []
    for ch in txt:
        codepoint = ord(ch)

        if not codepoint:
            chars.append('\x00')
            continue

        try:
            chars.append(_replaces[codepoint-1])
        except IndexError:
            pass
    return "".join(chars)
