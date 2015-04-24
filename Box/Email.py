__author__ = 'angeloluna'

import datetime


class Email(object):
    def __init__(self, sAddr, rAddr, subject, message, attachment):
        self.sAddr = sAddr
        self.rAddr = rAddr
        self.subject = subject
        self.message = message
        self.attachment = attachment

        self.time = datetime.now().time()


    def reply(self):
        pass

    def forward(self):
        pass



