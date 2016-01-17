from __future__ import unicode_literals

import platform
import os

import semver


VENDOR_PATH = os.path.join(os.path.dirname(__file__), 'vendor')


class UNotifier(object):

    def __new__(cls, *args, **kwds):
        from . import notifiers

        system = platform.system()

        if system == 'Linux':
            cls = notifiers.NotifySendNotifier
        elif system == 'Darwin':
            cls = notifiers.NotificationCenterNotifier
        elif system == 'Windows':
            if semver.match(platform.release(), '<6.2.9200'):
                cls = notifiers.BalloonNotifier
            else:
                cls = notifiers.ToasterNotifier
        else:
            cls = notifiers.GrowlNotifier

        return cls(*args, **kwds)
