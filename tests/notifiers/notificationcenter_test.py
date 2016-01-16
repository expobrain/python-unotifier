from __future__ import unicode_literals

import unittest
import os

from unotifier import VENDOR_PATH
from unotifier.notifiers import NotificationCenterNotifier

from . import NotifierTestsMixin


class NotificationCenterNotifierTests(NotifierTestsMixin, unittest.TestCase):

    notifier_klass = NotificationCenterNotifier
    notifier_cmd = os.path.join(
        VENDOR_PATH,
        'terminal-notifier.app', 'Contents', 'MacOS', 'terminal-notifier'
    )
