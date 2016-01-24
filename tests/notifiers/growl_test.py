from __future__ import unicode_literals

import unittest

from unotifier.notifiers import GrowlNotifier

from . import NotifierTestsMixin


class GrowlNotifierTests(NotifierTestsMixin, unittest.TestCase):

    notifier_klass = GrowlNotifier

    def setUp(self):
        super(GrowlNotifierTests, self).setUp()

    def tearDown(self):
        super(GrowlNotifierTests, self).tearDown()

    def test_notify(self):
        pass
