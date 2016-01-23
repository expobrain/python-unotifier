from __future__ import unicode_literals

import os
import platform

from .. import VENDOR_PATH
from .abstract import AbstractNotifier


class BalloonNotifier(AbstractNotifier):

    DEFAULT_TITLE = 'Node Notification:'

    @property
    def notifier_cmd(self):
        return os.path.join(
            VENDOR_PATH,
            'notifu',
            'notifu{}.exe'.format(
                '64' if platform.architecture()[0] == '64bit' else ''
            )
        )

    def get_cmd_options(self, options):
        options = self._map_app_icon(options)
        options = self._map_text(options)

        if 'icon' in options:
            options['i'] = options.pop('icon')

        if 'message' in options:
            options['m'] = options.pop('message')

        if options.get('title'):
            options['p'] = options.pop('title')
        else:
            options['p'] = self.DEFAULT_TITLE

        if 'time' in options:
            options['d'] = options.pop('time')

        if options.pop('q', None):
            options['q'] = True

        if options.pop('quiet', None):
            options.pop('q')

        if options.pop('sound', None):
            options.pop('q')

        if options.get('t'):
            options['d'] = options.pop('t')

        return options
