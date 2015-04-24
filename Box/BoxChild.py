__author__ = 'angeloluna'

from Box import Box


class Inbox(Box):
    """email inbox"""
    def __init__(self):
        super(Box, self).__init__()
        self.name = "inbox"
        self.location = "location"


class Sent(Box):
    """emails send out will be saved here"""
    def __init__(self):
        super(Box, self).__init__()
        self.name = "Sent"
        self.location = "location"


class Drafts(Box):
    """email drafts saved here"""
    def __init__(self):
        super(Box, self).__init__()
        self.name = "Drafts"
        self.location = "location"


class Trash(Box):
    """deleted emails are saved here"""
    def __init__(self):
        super(Box, self).__init__()
        self.name = "Trash"
        self.location = "location"



