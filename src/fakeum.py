#!/usr/bin/python
# encoding: utf-8
#
# Copyright (c) 2014 deanishe@deanishe.net
#
# MIT Licence. See http://opensource.org/licenses/MIT
#
# Created on 2014-12-29
#

"""Alfred 3 workflow to generate test data."""

from __future__ import print_function, absolute_import

from collections import OrderedDict
import datetime
import random
import sys

from workflow import Workflow3, ICON_WARNING, MATCH_ALL, MATCH_ALLCHARS

from common import (
    DEFAULT_SETTINGS,
    ISSUE_URL,
    UPDATE_SETTINGS,
    intvar,
    run_workflow,
)

# Query delimiter that separates faker name from quantity
DELIMITER = u'✕'

# Number of sentences per paragraph of Lipsum text
LIPSUMS = intvar('LIPSUM_SENTENCES', 3)

# ALFRED_AS = 'tell application "Alfred 2" to search "fake "'

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


def all_fakers():
    """Return all fakers."""
    from faker import Factory
    global fakers
    if not fakers:
        for loc in wf.settings.get('locales', DEFAULT_SETTINGS['locales']):
            fakers.append(Factory.create(loc))

    return fakers


def get_faker(name=None):
    """Return random faker instance."""
    fakers = all_fakers()

    if name is None:
        return random.choice(fakers)

    random.shuffle(fakers)
    methname = FAKERS[name]
    for faker in fakers:
        if hasattr(faker, methname):
            return faker


# def run_workflow():
#     """Run workflow in Alfred"""
#     subprocess.call(['osascript', '-e', ALFRED_AS])


def get_fake_datum(name):
    """Return one fake datum for name."""
    faker = get_faker(name)
    if not faker:
        return None

    methname = FAKERS[name]
    if name == 'Paragraph':  # Pass no. of sentences to generator
        datum = getattr(faker, methname)(LIPSUMS, False)
    else:
        datum = getattr(faker, methname)()

    if isinstance(datum, int):
        datum = str(datum)

    elif isinstance(datum, datetime.datetime):
        datum = datum.strftime('%Y-%m-%d %H:%M:%S')

    elif not isinstance(datum, basestring):
        log.debug(u'%s : (%s) %r', name, datum.__class__, datum)

    return datum


def supported_type(name):
    """Return ``True`` if at least one Faker supports this type."""
    methname = FAKERS[name]
    for faker in all_fakers():
        if hasattr(faker, methname):
            return True

    log.debug('data type "%s" is not supported by active locales', name)
    return False


def get_fake_data(names=None, count=1):
    """Return list of fake data."""
    fake_data = []

    if not names:
        names = sorted(FAKERS.keys())

    names = [n for n in names if supported_type(n)]

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
    """Run workflow."""
    if wf.update_available:
        wf.add_item('A newer version is available',
                    u'↩ to install update',
                    autocomplete='workflow:update',
                    icon='update-available.png')

    query = None

    if len(wf.args):
        query = wf.args[0]

    log.debug('query=%r', query)

    count = 0

    if DELIMITER in query:
        if query.endswith(DELIMITER):
            # Run workflow with previous query
            # run_workflow(wf.cached_data('last_query', session=True))
            run_workflow()
            return

        query, count = [s.strip() for s in query.split(DELIMITER)]

        if count:
            if not count.isdigit():
                wf.add_item(u'Not a number : ' + count,
                            'Please enter a number',
                            icon=ICON_WARNING)
                wf.send_feedback()
                return

            count = int(count)
        else:
            count = 1

        fake_data = get_fake_data(names=[query], count=count)

    else:
        # Save last query so we can jump back to it if user backs up
        # wf.cache_data('last_query', query, session=True)

        fake_data = get_fake_data()

        if query:

            fake_data = wf.filter(query, fake_data,
                                  lambda t: t[0],
                                  match_on=MATCH_ALL ^ MATCH_ALLCHARS,
                                  min_score=20)

    log.debug('count=%d', count)

    if not fake_data:
        wf.add_item('No matching fakers',
                    'Try a different query',
                    icon=ICON_WARNING)

    for name, data in fake_data:

        subtitle = data
        if count:
            example = data.split('\n')[0].strip()
            subtitle = u'{} ✕ e.g. "{}"'.format(count, example)

        it = wf.add_item(name,
                         subtitle,
                         arg=data,
                         autocomplete=u'{} {} '.format(name, DELIMITER),
                         valid=True,
                         largetext=data,
                         copytext=data)

        it.setvar('title', 'Copied to Clipboard')
        it.setvar('text', data)

        mod = it.add_modifier('cmd', 'Paste to frontmost application')
        mod.setvar('paste', 1)
        mod.setvar('SHOW_NOTIFICATIONS', 0)

    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow3(default_settings=DEFAULT_SETTINGS,
                   update_settings=UPDATE_SETTINGS,
                   help_url=ISSUE_URL,
                   libraries=['./libs'])
    log = wf.logger
    sys.exit(wf.run(main))
