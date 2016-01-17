from __future__ import unicode_literals

import subprocess


class AbstractNotifier(object):

    CLI_OPTION_CHAR = '--'
    NOTIFIER_CMD = None
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
        self.options = dict(options) if options else {}

    def _map_app_icon(self, options):
        options = dict(options)

        if 'appIcon' in options:
            options['icon'] = options.pop('appIcon')

        return options

    def _map_icon_shorthand(self, options):
        options = dict(options)

        if 'i' in options:
            options['icon'] = options.pop('i')

        return options

    def _map_text(self, options):
        options = dict(options)

        if 'text' in options:
            options['icon'] = options.pop('text')

        return options

    def get_cmd_args(self, options):
        options = dict(options)
        args = []

        for k, v in options.iteritems():
            if v is not None:
                args.append('{}{}'.format(self.CLI_OPTION_CHAR, k))
                args.append('"{}"'.format(v))

        return args

    def get_options(self):
        opts = dict(self.DEFAULT_OPTIONS)
        opts.update(self.options)

        return opts

    def notify(self, message, title=None, icon=None, wait=None):
        options = self.get_options()
        options['message'] = message
        options['title'] = title
        options['icon'] = icon

        args = [self.NOTIFIER_CMD]
        args.extend(self.get_cmd_args(options))

        subprocess.check_call(args)
