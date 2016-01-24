from __future__ import unicode_literals

import gntp.notifier

from .abstract import AbstractNotifier


class GrowlNotifier(AbstractNotifier):

    DEFAULT_APP_NAME = 'Python'
    DEFAULT_HOSTNAME = 'localhost'

    def __init__(self, *args, **kwds):
        super(GrowlNotifier, self).__init__(*args, **kwds)

        options = kwds.get('options', {})

        self.growl = gntp.notifier.GrowlNotifier(
            applicationName=options.get('name', self.DEFAULT_APP_NAME),
            hostname=options.get('host', self.DEFAULT_HOSTNAME)
        )
        self.growl.register()

    def get_cmd_options(self, options):
        options = self._map_app_icon(options)
        options = self._map_icon_shorthand(options)

        if options.get('text'):
            options['message'] = options.pop('text')

        return options

    def notify(self, message, title=None, icon=None, wait=None):
        # Prepare options
        options = self.options
        options['message'] = message
        options['title'] = title
        options['icon'] = icon

        # Get command options
        cmd_options = self.get_cmd_options(options)

        self.growl.notify(**cmd_options)
