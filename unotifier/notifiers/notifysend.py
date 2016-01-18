from __future__ import unicode_literals

import os

from .. import VENDOR_PATH
from .abstract import AbstractNotifier


class NotifySendNotifier(AbstractNotifier):

    NOTIFIER_CMD = os.path.join(VENDOR_PATH, 'notify-send')

    def get_cmd_options(self, options):
        options = self._map_app_icon(options)
        options = self._map_text(options)

        return options
