from __future__ import unicode_literals

import unittest

from mock import patch

from unotifier import UNotifier, notifiers


class UNotifierTests(unittest.TestCase):

    def test_linux(self):
        with patch('platform.system', return_value='Linux'):
            notifier = UNotifier()

            assert isinstance(notifier, notifiers.NotifySendNotifier)

    def test_darwin(self):
        with patch('platform.system', return_value='Darwin'):
            notifier = UNotifier()

            assert isinstance(notifier, notifiers.NotificationCenterNotifier)

    def test_windows_8_1(self):
        with patch('platform.system', return_value='Windows'):
            with patch('platform.release', return_value='6.3.9600'):
                notifier = UNotifier()

                assert isinstance(notifier, notifiers.ToasterNotifier)

    def test_windows_8(self):
        with patch('platform.system', return_value='Windows'):
            with patch('platform.release', return_value='6.2.9200'):
                notifier = UNotifier()

                assert isinstance(notifier, notifiers.ToasterNotifier)

    def test_windows_before_8(self):
        with patch('platform.system', return_value='Windows'):
            with patch('platform.release', return_value='6.1.7601'):
                notifier = UNotifier()

                assert isinstance(notifier, notifiers.BalloonNotifier)

    def test_default_growl(self):
        with patch('platform.system', return_value=''):
            notifier = UNotifier()

            assert isinstance(notifier, notifiers.GrowlNotifier)
