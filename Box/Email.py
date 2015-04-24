__author__ = 'angeloluna'

class Email(object):
    def __init__(self, sAddr, rAddr, subject, message, attachment):
        self.sAddr = sAddr
        self.rAddr = rAddr
        self.subject = subject
        self.message = message
        self.attachment = attachment

    def move(self, box):
        pass

    def copy(self, box):
        pass

    def send(self):
        pass