__author__ = 'angeloluna'

import datetime
import Box

class Email(object):
    def __init__(self, sAddr, rAddr, subject, message, attachment):
        self.sAddr = sAddr
        self.rAddr = rAddr
        self.subject = subject
        self.message = message
        self.attachment = attachment

        self.time = datetime.datetime.now()

        self.isRead = True

    def reply(self):
        Box.write()

    def forward(self):
        Box.write()
        pass

    def read(self):
        self.isRead = False
    
    def to_object(self, email):
        """takes an email and creates an email object"""
        pass

    def to_email(self, object):
        """takes an email object and creates an email"""
        pass

    def print_email(self):
        print('subject' + 'message')

