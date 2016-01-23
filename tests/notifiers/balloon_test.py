from __future__ import unicode_literals

import platform
import unittest
import os

import mock

from unotifier import VENDOR_PATH
from unotifier.notifiers import BalloonNotifier

from . import NotifierTestsMixin


class BalloonNotifierTests(NotifierTestsMixin, unittest.TestCase):

    notifier_klass = BalloonNotifier
    base_notifier_cmd = os.path.join(VENDOR_PATH, 'notifu', 'notifu{}.exe')

    @property
    def notifier_cmd(self):
        if platform.architecture()[0] == '64bit':
            return self.base_notifier_cmd.format('64')

        return self.base_notifier_cmd.format('')

    @mock.patch('platform.architecture', return_value=('64bit',))
    def test_notifier_cmd(self, m_architecture):
        cmd = self.notifier_klass().notifier_cmd
        expected = self.base_notifier_cmd.format('64')

        assert cmd == expected

    @mock.patch('platform.architecture', return_value=('32bit',))
    def test_notifier_cmd_32(self, m_architecture):
        cmd = self.notifier_klass().notifier_cmd
        expected = self.base_notifier_cmd.format('')

        assert cmd == expected

    @mock.patch('platform.architecture', return_value=('64bit',))
    def test_notify(self, m_architecture):
        super(BalloonNotifierTests, self).test_notify()

    @mock.patch('platform.architecture', return_value=('32bit',))
    def test_notify_32bit(self, m_architecture):
        super(BalloonNotifierTests, self).test_notify()
