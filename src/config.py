#!/usr/bin/python
# encoding: utf-8
#
# Copyright © 2014 deanishe@deanishe.net
#
# MIT Licence. See http://opensource.org/licenses/MIT
#
# Created on 2014-12-29
#

"""config.py [options] [args]

Usage:
    config.py --toggle <locale>
    config.py <query>

Options:
    --toggle <locale>   Turn locale on/off
    -h, --help          Show this help message
"""

from __future__ import print_function, unicode_literals, absolute_import


import subprocess
import sys

from workflow import Workflow
from fakeum import ALL_LOCALES, DEFAULT_SETTINGS, UPDATE_SETTINGS, HELP_URL

ALFRED_AS = 'tell application "Alfred 2" to search "fakeconfig "'

log = None


def main(wf):
    from docopt import docopt
    args = docopt(__doc__, wf.args)

    log.debug('args : {!r}'.format(args))

    if args.get('--toggle'):
        loc = args.get('--toggle')
        active = wf.settings.get('locales', [])
        is_active = loc in active

        if is_active:
            msg = 'Deactivated locale {}'.format(ALL_LOCALES.get(loc))
            active.remove(loc)
            wf.settings['locales'] = active
        else:
            msg = 'Activated locale {}'.format(ALL_LOCALES.get(loc))
            active.append(loc)
            wf.settings['locales'] = active

        log.info(msg)
        print(msg)

        subprocess.call(['osascript', '-e', ALFRED_AS])
        return 0

    if wf.update_available:
        wf.add_item('A newer version is available',
                    '↩ to install update',
                    autocomplete='workflow:update',
                    icon='update-available.png')

    query = args.get('<query>')

    locales = sorted([(v, k) for (k, v) in ALL_LOCALES.items()])

    if query:

        locales = wf.filter(query, locales, key=lambda t: '{} {}'.format(*t),
                            min_score=30)

    for name, loc in locales:
        if loc in wf.settings.get('locales', []):
            icon = 'active.png'
        else:
            icon = 'inactive.png'
        wf.add_item(name, loc,
                    arg=loc,
                    valid=True,
                    icon=icon)

    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow(default_settings=DEFAULT_SETTINGS,
                  update_settings=UPDATE_SETTINGS,
                  help_url=HELP_URL)
    log = wf.logger
    sys.exit(wf.run(main))
