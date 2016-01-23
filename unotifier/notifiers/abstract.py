from __future__ import unicode_literals

import subprocess


class AbstractNotifier(object):

    CLI_OPTION_CHAR = '--'
    notifier_cmd = None
    DEFAULT_OPTIONS = {
        'title': None,
        'subtitle': None,
        'message': None,
        'sound': False,  # Case Sensitive string of sound file
        'icon': None,  # Set icon? (Absolute path to image)
        'contentImage': None,  # Attach image? (Absolute path)
        'open': None,  # URL to open on click
        'wait': False  # if wait for notification to end
    }

    def __init__(self, options=None):
        self._options = dict(options) if options else {}

    @property
    def options(self):
        opts = dict(self.DEFAULT_OPTIONS)
        opts.update(self._options)

        return opts

    def _map_app_icon(self, options):
        options = dict(options)
        options['icon'] = options.pop('appIcon', None)

        return options

    def _map_icon_shorthand(self, options):
        options = dict(options)
        options['icon'] = options.pop('i', None)

        return options

    def _map_text(self, options):
        options = dict(options)
        options['message'] = options.pop('text', None)

        return options

    def get_cmd_options(self, options):
        return options

    def build_cmd_args(self, options):
        args = []

        for k, v in options.iteritems():
            if v is not None:
                args.append('{}{}'.format(self.CLI_OPTION_CHAR, k))
                args.append('"{}"'.format(v))

        return args

    def notify(self, message, title=None, icon=None, wait=None):
        # Prepare options
        options = self.options
        options['message'] = message
        options['title'] = title
        options['icon'] = icon

        # Get command options
        cmd_options = self.get_cmd_options(options)

        # Build cmd args
        cmd_args = self.build_cmd_args(cmd_options)

        # Call notifier
        subprocess.check_call([self.notifier_cmd] + cmd_args)
