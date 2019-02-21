#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2017 Dean Jackson <deanishe@deanishe.net>
#
# MIT Licence. See http://opensource.org/licenses/MIT
#
# Created on 2017-11-14
#

"""Common workflow variables and functions."""

from __future__ import print_function, absolute_import

from collections import OrderedDict
import logging
import os

from workflow import Variables
from workflow.util import run_applescript


log = logging.getLogger('workflow')


# Default workflow settings
DEFAULT_SETTINGS = {
    'locales': [
        'en',
        'de_DE',
        'es_ES',
        'fr_FR',
    ],
}

DOCS_URL = 'https://github.com/deanishe/alfred-fakeum/blob/master/README.md'
HELP_URL = u'https://www.alfredforum.com/topic/5319-fakeum-—-generate-fake-test-datasets-in-alfred/'
ISSUE_URL = 'https://github.com/deanishe/alfred-fakeum/issues'
UPDATE_SETTINGS = {'github_slug': 'deanishe/alfred-fakeum'}

# Workflow icons
ICON_DOCS = 'icons/docs.png'
ICON_HELP = 'icons/help.png'
ICON_ISSUE = 'icons/issue.png'
ICON_ON = 'icons/on.png'
ICON_OFF = 'icons/off.png'
ICON_LOCALES = 'icons/locales.png'
ICON_UPDATE_CHECK = 'icons/update-check.png'
ICON_UPDATE_AVAILABLE = 'icons/update-available.png'

# All locales supported by faker
ALL_LOCALES = OrderedDict((
    ('en', 'English'),
    ('de_DE', 'German'),
    ('es', 'Spanish'),
    ('fr_FR', 'French'),
    ('ar_AA', 'Arabic'),
    ('ar_EG', 'Arabic (Egypt)'),
    ('ar_JO', 'Arabic (Jordan)'),
    ('ar_PS', 'Arabic (Palestine)'),
    ('ar_SA', 'Arabic (Saudi Arabia)'),
    ('bs_BA', 'Bosnian'),
    ('bg_BG', 'Bulgarian'),
    ('zh_CN', 'Chinese (China)'),
    ('zh_TW', 'Chinese (Taiwan)'),
    ('hr_HR', 'Croatian'),
    ('cs_CZ', 'Czech'),
    ('dk_DK', 'Danish'),
    ('nl_NL', 'Dutch'),
    ('nl_BE', 'Dutch (Belgium)'),
    ('en_AU', 'English (Australia)'),
    ('en_CA', 'English (Canada)'),
    ('en_GB', 'English (Great Britain)'),
    ('en_TH', 'English (Thailand)'),
    ('en_US', 'English (United States)'),
    ('et_EE', 'Estonian'),
    ('fi_FI', 'Finnish'),
    ('fr_CH', 'French (Switzerland)'),
    ('ka_GE', 'Georgian'),
    ('de_AT', 'German (Austria)'),
    ('tw_GH', 'Ghanaian'),
    ('el_GR', 'Greek'),
    ('he_IL', 'Hebrew'),
    ('hi_IN', 'Hindi'),
    ('hu_HU', 'Hungarian'),
    ('id_ID', 'Indonesian'),
    ('it_IT', 'Italian'),
    ('ja_JP', 'Japanese'),
    ('ko_KR', 'Korean'),
    ('la', 'Latin'),
    ('lv_LV', 'Latvian'),
    ('lt_LT', 'Lithuanian'),
    ('ne_NP', 'Nepali'),
    ('no_NO', 'Norwegian'),
    ('fa_IR', 'Persian'),
    ('pl_PL', 'Polish'),
    ('pt_BR', 'Portuguese (Brazil)'),
    ('pt_PT', 'Portuguese (Portugal)'),
    ('ru_RU', 'Russian'),
    ('sk_SK', 'Slovakian'),
    ('sl_SI', 'Slovenian'),
    ('es_MX', 'Spanish (Mexico)'),
    ('es_ES', 'Spanish (Spain)'),
    ('sv_SE', 'Swedish'),
    ('th_TH', 'Thai'),
    ('tr_TR', 'Turkish'),
    ('uk_UA', 'Ukranian'),
))


# Workflow's bundle IDs
BUNDLE_ID = os.getenv('alfred_workflow_bundleid')

# Script Filter keyword
KEYWORD = os.getenv('keyword')

# AppleScript to run an Alfred search
SEARCH_AS = u'tell application "Alfred 3" to search "{query}"'


def boolvar(name, default=False):
    """Return `True` or `False` for a workflow variable."""
    v = os.getenv(name)
    if v is not None:
        if v.lower() in ('1', 'on', 'yes'):
            return True

        if v.lower() in ('0', 'off', 'no'):
            return False
    log.debug('no value set for workflow variable "%s", '
              'using default: %r', name, default)
    return default


def intvar(name, default=0):
    """Return `int` for a workflow variable."""
    v = os.getenv(name)
    if v is not None:
        try:
            v = int(v)
        except ValueError:
            log.error('bad value for "%s": "%s" is not a number', name, v)
            return default
        return v
    log.debug('no value set for workflow variable "%s", '
              'using default: %r', name, default)
    return default


def run_workflow(query=None):
    """Run workflow with query."""
    query = KEYWORD + u' ' + (query or '')
    script = SEARCH_AS.format(query=query)
    log.debug(u'calling Alfred with query "%s" ...', query)
    run_applescript(script)


def notify(title, text=''):
    """Show a notification."""
    if not boolvar('SHOW_NOTIFICATIONS'):
        return

    v = Variables(title=title, text=text)
    print(v)
