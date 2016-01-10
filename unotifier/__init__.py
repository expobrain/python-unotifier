from __future__ import unicode_literals

import platform

import semver

from . import notifiers


class UNotifier(object):

    def __new__(cls, *args, **kwds):
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

        return cls.__new__(cls, *args, **kwds)
