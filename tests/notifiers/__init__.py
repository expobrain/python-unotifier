from __future__ import unicode_literals

import os
import inspect

from mock import patch
import six


VENDOR_PATH = os.path.join(
    os.path.dirname(__file__), '..', '..', 'unotifier', 'vendor'
)


class NotifierTestsMixin(object):

    notifier_klass = None
    notifier_cmd = None

    def setUp(self):
        super(NotifierTestsMixin, self).setUp()

        if not inspect.isclass(self.notifier_klass):
            raise AttributeError("Attribute `notifier_klass` not set")

        if not isinstance(self.notifier_cmd, six.string_types):
            raise AttributeError("Attribute `notifier_cmd` not set")

        self.notifier = self.notifier_klass()

    def test_notify(self):
        message = 'test message'
        title = 'test title'
        icon = os.path.join(os.path.dirname(__file__), 'icon.png')

        with patch('subprocess.check_call') as m_check_call:
            self.notifier.notify(message, title=title, icon=icon)

            options = self.notifier.get_options()
            options['message'] = message
            options['title'] = title
            options['icon'] = icon

            cmd_args = [self.notifier_cmd]
            cmd_args.extend(self.notifier.get_cmd_args(options))

            m_check_call.assert_called_once_with(cmd_args)
