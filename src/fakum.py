#!/usr/bin/python
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

from collections import OrderedDict
import datetime
import random
import subprocess
import sys

from workflow import Workflow, ICON_WARNING, MATCH_ALL, MATCH_ALLCHARS
from faker import Factory

DELIMITER = '⟩'

HELP_URL = 'https://github.com/deanishe/alfred-fakum'
UPDATE_SETTINGS = {'github_slug': 'deanishe/alfred-fakum'}

# All locales supported by faker
ALL_LOCALES = {
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


DEFAULT_SETTINGS = {
    'locales': [
        # 'en_GB',
        'en_US',
        'de_DE',
        'it_IT',
        'es_ES',
        # 'fr_FR',
    ],
}

ALFRED_AS = 'tell application "Alfred 2" to search "fake "'

FAKERS = OrderedDict([
    # People
    ('Name', 'name'),
    ('First Name', 'first_name'),
    ('Last Name', 'last_name'),
    ('Email', 'email'),
    ('Email (corporate)', 'company_email'),
    ('Email (free)', 'free_email'),
    ('Email (safe)', 'safe_email'),
    ('Email domain (free)', 'free_email_domain'),
    # Addresses
    ('Address', 'address'),
    ('Street', 'street_address'),
    ('Street Name', 'street_name'),
    ('City', 'city'),
    ('State', 'state'),
    ('State abbr.', 'state_abbr'),
    ('Country', 'country'),
    # Internet
    ('TLD', 'tld'),
    ('Domain Name', 'domain_name'),
    ('Domain Word', 'domain_word'),
    ('IP Address (IPv4)', 'ipv4'),
    ('IP Address (IPv6)', 'ipv6'),
    ('URI', 'uri'),
    ('URI path', 'uri_path'),
    ('URL', 'url'),
    # Corporate bullshit
    ('Corporate BS', 'bs'),
    ('Corporate catchphrase', 'catch_phrase'),
    ('Company', 'company'),
    ('Company suffix', 'company_suffix'),
    # Lorem
    ('Paragraph', 'paragraph'),
    # 'Paragraphs', 'paragraphs',
    ('Sentence', 'sentence'),
    # 'Sentences', 'sentences',
    # 'Text', 'text',
    ('Word', 'word'),
    # 'Words', 'words',
    # Dates and times
    ('Date', 'date'),
    ('Datetime', 'date_time'),
    ('ISO 8601 Datetime', 'iso8601'),
    ('Time', 'time'),
    ('Timezone', 'timezone'),
    ('UNIX timestamp', 'unix_time'),
])

log = None
fakers = []


def get_faker():
    """Return random faker instance"""
    global fakers
    if not fakers:
        for loc in wf.settings.get('locales', ALL_LOCALES):
            fakers.append(Factory.create(loc))

    return random.choice(fakers)


def run_workflow():
    """Run workflow in Alfred"""
    subprocess.call(['osascript', '-e', ALFRED_AS])


def get_fake_datum(name):
    """Return one fake datum for name"""

    methname = FAKERS[name]
    # Get a faker instance that has the required method
    while True:
        faker = get_faker()
        if hasattr(faker, methname):
            datum = getattr(faker, methname)()
            break

    if isinstance(datum, int):
        datum = '{}'.format(datum)

    elif isinstance(datum, datetime.datetime):
        datum = '{}'.format(datum.strftime('%Y-%m-%d %H:%M:%S'))

    elif not isinstance(datum, basestring):
        log.debug('{} : ({}) {!r}'.format(name,
                                          datum.__class__,
                                          datum))

    return datum


def get_fake_data(names=None, count=1):
    """Return list of fake data"""

    fake_data = []

    if not names:
        names = sorted(FAKERS.keys())

    for name in names:

        data = []
        for i in range(count):
            data.append(get_fake_datum(name))

        if name in ('Paragraph', 'Address'):
            data = '\n\n'.join(data)
        else:
            data = '\n'.join(data)

        fake_data.append((name, data))

    return fake_data


def main(wf):

    if wf.update_available:
        wf.add_item('An newer version is available',
                    '↩ to install update',
                    autocomplete='workflow:update',
                    icon='update-available.png')

    query = None
    if len(wf.args):
        query = wf.args[0]

    log.debug('query : {!r}'.format(query))

    count = None

    if DELIMITER in query:
        if query.endswith(DELIMITER):
            run_workflow()
            return 0

        query, count = [s.strip() for s in query.split(DELIMITER)]

        if count:
            if not count.isdigit():
                wf.add_item('Not a number : {}'.format(count),
                            'Please enter a number',
                            icon=ICON_WARNING)
                wf.send_feedback()
                return 0

            count = int(count)
        else:
            count = 1

        fake_data = get_fake_data(names=[query], count=count)

    else:
        fake_data = get_fake_data()

        if query:

            fake_data = wf.filter(query, fake_data,
                                  lambda t: t[0],
                                  match_on=MATCH_ALL ^ MATCH_ALLCHARS,
                                  min_score=20)

    log.debug('count : {!r}'.format(count))

    if not fake_data:
        wf.add_item('No matching fake data',
                    'Try a different query',
                    icon=ICON_WARNING)

    for name, data in fake_data:

        subtitle = data
        if count:
            example = data.split('\n')[0].strip()
            subtitle = '{} ✕ e.g. "{}"'.format(count, example)

        wf.add_item(name,
                    subtitle,
                    arg=data,
                    autocomplete='{} {} '.format(name, DELIMITER),
                    valid=True,
                    largetext=data,
                    copytext=data)

    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow(default_settings=DEFAULT_SETTINGS,
                  update_settings=UPDATE_SETTINGS,
                  help_url=HELP_URL)
    log = wf.logger
    sys.exit(wf.run(main))
