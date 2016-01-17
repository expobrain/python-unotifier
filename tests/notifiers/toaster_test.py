from __future__ import unicode_literals

import os
import unittest

from unotifier import VENDOR_PATH
from unotifier.notifiers import ToasterNotifier

from . import NotifierTestsMixin


class ToasterNotifierTests(NotifierTestsMixin, unittest.TestCase):

    notifier_klass = ToasterNotifier
    notifier_cmd = os.path.join(VENDOR_PATH, 'toaster', 'toast.exe')
