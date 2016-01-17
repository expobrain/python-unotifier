from __future__ import unicode_literals

import os

from .. import VENDOR_PATH
from .abstract import AbstractNotifier


class ToasterNotifier(AbstractNotifier):

    NOTIFIER_CMD = os.path.join(VENDOR_PATH, 'toaster', 'toast.exe')

    def notify(self, message, *args, **kwds):

        super(ToasterNotifier, self).notify(message, *args, **kwds)

    def get_cmd_args(self, options):
        options = self._map_app_icon(options)
        options = self._map_text(options)

        options['p'] = options.pop('icon', None)
        options['t'] = options.pop('title', None)
        options['w'] = options.pop('wait', None)

        # Remove escape char to debug "HRESULT : 0xC00CE508" exception
        options['m'] = (options.get('message') or '').replace('\x1b', '')

        if (not options.get('sound')
                and (options.get('quiet') or options.get('silent'))):

            options['q'] = True
            options.pop('quiet', None)
            options.pop('silent', None)

        options.pop('sound', None)

        return options
