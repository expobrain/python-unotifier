from __future__ import unicode_literals

import os

from .. import VENDOR_PATH
from .abstract import AbstractNotifier


class NotificationCenterNotifier(AbstractNotifier):

    DEFAULT_SOUND = 'Bottle'
    CLI_OPTION_CHAR = '-'
    NOTIFIER_CMD = os.path.join(
        VENDOR_PATH,
        'terminal-notifier.app', 'Contents', 'MacOS', 'terminal-notifier'
    )

    def get_options(self):
        options = super(NotificationCenterNotifier, self).get_options()

        options = self._map_icon_shorthand(options)
        options = self._map_text(options)

        if 'icon' in options:
            options['appIcon'] = options.pop('icon')

        if options.get('sound') is True:
            options['sound'] = self.DEFAULT_SOUND
        elif options.get('sound') is False:
            del options['sound']

        return options
