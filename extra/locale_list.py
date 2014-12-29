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
Generate a list of locales supported by Faker
"""

from __future__ import print_function, unicode_literals, absolute_import

from pprint import pprint
import re
import sys
import os

dirpath = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                       'src', 'faker', 'providers')

is_locale = re.compile(r'[a-z]{2}_[A-Z]{2}').match

locale_names = {
    'bg_BG': 'Bulgarian',
    'cs_CZ': 'Czech',
    'de_DE': 'German',
    'dk_DK': 'Danish',
    'el_GR': 'Greek',
    'en_CA': 'English (CA)',
    'en_GB': 'English (GB)',
    'en_US': 'English (US)',
    'es_ES': 'Spanish (ES)',
    'es_MX': 'Spanish (MX)',
    'fa_IR': 'Persian',
    'fi_FI': 'Finnish',
    'fr_FR': 'French',
    'hi_IN': 'Hindi',
    'it_IT': 'Italian',
    'ko_KR': 'Korean',
    'lt_LT': 'Lithuanian',
    'lv_LV': 'Latvian',
    'nl_NL': 'Dutch',
    'no_NO': 'Norwegian',
    'pl_PL': 'Polish',
    'pt_BR': 'Portuguese (BR)',
    'ru_RU': 'Russian',
    'sl_SI': 'Slovenian',
    'zh_CN': 'Chinese (CN)',
    'zh_TW': 'Chinese (TW)',
}


def main():
    locales = {}
    for filename in os.listdir(dirpath):
        path = os.path.join(dirpath, filename)
        if not os.path.isdir(path) or not is_locale(filename):
            continue
        locales[filename] = locale_names.get(filename, '')

    pprint(locales)


if __name__ == '__main__':
    sys.exit(main())
