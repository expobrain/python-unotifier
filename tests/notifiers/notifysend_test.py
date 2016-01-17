from __future__ import unicode_literals

import os
import unittest

from unotifier import VENDOR_PATH
from unotifier.notifiers import NotifySendNotifier

from . import NotifierTestsMixin


class NotifySendNotifierTests(NotifierTestsMixin, unittest.TestCase):

    notifier_klass = NotifySendNotifier
    notifier_cmd = os.path.join(VENDOR_PATH, 'notify-send')
