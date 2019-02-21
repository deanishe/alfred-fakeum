#!/usr/bin/python
# encoding: utf-8
#
# Copyright (c) 2014 deanishe@deanishe.net
#
# MIT Licence. See http://opensource.org/licenses/MIT
#
# Created on 2014-12-29
#

"""config.py [options] [args]

Show and alter configuration options.

Usage:
    config.py locales [<query>]
    config.py settings [<query>]
    config.py --toggle-locale <locale>
    config.py --toggle-notifications

Options:
    -l, --toggle-locale <locale>   Turn locale on/off
    -n, --toggle-notifications     Turn notifications on/off
    -h, --help                     Show this help message and exit
"""

from __future__ import print_function, absolute_import


import sys

from workflow import Workflow3, ICON_WARNING
from workflow.util import run_trigger, set_config

from common import (
    ALL_LOCALES,
    DEFAULT_SETTINGS,
    DOCS_URL,
    HELP_URL,
    ISSUE_URL,
    ICON_DOCS,
    ICON_HELP,
    ICON_ISSUE,
    ICON_ON,
    ICON_OFF,
    ICON_LOCALES,
    ICON_UPDATE_AVAILABLE,
    ICON_UPDATE_CHECK,
    UPDATE_SETTINGS,
    boolvar,
)


log = None


def filter_options(query):
    """Show available options."""
    options = []
    if wf.update_available:
        title = 'An update is available'
        subtitle = u'↩ or ⇥ to install update'
        icon = ICON_UPDATE_AVAILABLE
    else:
        title = 'Check for update'
        subtitle = u'↩ or ⇥ to check for update'
        icon = ICON_UPDATE_CHECK

    options = [
        dict(title=title,
             subtitle=subtitle,
             valid=False,
             autocomplete='workflow:update',
             icon=icon),

        dict(title='Notifications',
             subtitle='Turn notifications on/off',
             valid=True,
             arg='notifications',
             icon=ICON_ON if boolvar('SHOW_NOTIFICATIONS') else ICON_OFF),

        dict(title='Locales',
             subtitle='Turn locales on/off',
             valid=True,
             arg='locales',
             icon=ICON_LOCALES),

        dict(title='Documentation',
             subtitle='Open workflow docs in browser',
             valid=True,
             arg=DOCS_URL,
             icon=ICON_DOCS),

        dict(title='Report Problem',
             subtitle='Open GitHub issues in browser',
             valid=True,
             arg=ISSUE_URL,
             icon=ICON_ISSUE),

        dict(title='Get Help',
             subtitle='Open Alfred forum thread in browser',
             valid=True,
             arg=HELP_URL,
             icon=ICON_HELP),
    ]

    if query:
        options = wf.filter(query, options, key=lambda d: d['title'],
                            min_score=30)

    if not options:
        wf.add_item('No matches', 'Try a different query?', valid=False,
                    icon=ICON_WARNING)

    for opt in options:
        wf.add_item(**opt)

    wf.send_feedback()


def filter_locales(query):
    """Show list of available locales."""
    locales = [(v, k) for (k, v) in ALL_LOCALES.items()]

    if query:

        locales = wf.filter(query, locales, key=lambda t: '{} {}'.format(*t),
                            min_score=30)

    if not locales:
        wf.add_item('No matches', 'Try a different query?', valid=False,
                    icon=ICON_WARNING)

    for name, loc in locales:
        icon = ICON_OFF
        if loc in wf.settings.get('locales', []):
            icon = ICON_ON

        wf.add_item(name, loc,
                    arg=loc,
                    valid=True,
                    icon=icon)

    wf.send_feedback()


def toggle_locale(loc):
    """Toggle a locale on or off."""
    active = wf.settings.get('locales', [])
    is_active = loc in active

    if is_active:
        log.info(u'Deactivated locale %s', ALL_LOCALES.get(loc))
        active.remove(loc)
        wf.settings['locales'] = active
    else:
        log.info(u'Activated locale %s', ALL_LOCALES.get(loc))
        active.append(loc)
        wf.settings['locales'] = active

    run_trigger('locales')


def toggle_notifications():
    """Turn notifications on/off."""
    name = 'SHOW_NOTIFICATIONS'
    is_active = boolvar(name)
    what = 'on'
    value = '1'

    if is_active:
        what = 'off'
        value = '0'

    set_config(name, value)
    log.info('turned notifications ' + what)

    run_trigger('config')


def main(wf):
    """Run configuration."""
    from docopt import docopt
    args = docopt(__doc__, wf.args)

    log.debug('args : %r', args)

    # ----------------------------------------------------------
    # Toggle actions

    if args.get('--toggle-locale'):
        return toggle_locale(args.get('--toggle-locale'))

    if args.get('--toggle-notifications'):
        return toggle_notifications()

    # ----------------------------------------------------------
    # List actions

    query = args.get('<query>')

    if args['settings']:
        return filter_options(query)

    else:
        return filter_locales(query)


if __name__ == '__main__':
    wf = Workflow3(default_settings=DEFAULT_SETTINGS,
                   update_settings=UPDATE_SETTINGS,
                   help_url=HELP_URL,
                   libraries=['./libs'])
    log = wf.logger
    sys.exit(wf.run(main))
