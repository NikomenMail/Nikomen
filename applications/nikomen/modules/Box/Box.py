__author__ = 'angeloluna'

from abc import ABCMeta, abstractmethod

class Box(object):
    """abstract box object used to create all the boxes to store emails in."""
    __metaclass__ = ABCMeta

    def add_email(self, email):
        self.emails.append(email)

    def filter(self, condition, item):
        """Filter email on conditions"""
        filtered_list = []

        if condition == 0:
            """filter by subject"""
            for i in xrange(len(self.emails)):
                if self.emails[i].subject.find(item) > -1:
                    filtered_list.append(self.emails[i])

        elif condition == 1:
            for i in xrange(len(self.emails)):
                if self.emails[i].sAddr.find(item) > -1:
                    filtered_list.append(self.emails[i])
        else:
            print('ERROR')

        Box.print_list(filtered_list)

    def sort(self, condition, rev):
        """sort email by conditions, 1 """

        if condition == 0:
            """sort by date"""
            self.emails.sort(key=lambda email: email.time, reverse=rev)
        elif condition == 1:
            """sort by subject"""
            self.emails.sort(key=lambda email: email.subject, reverse=rev)
        elif condition == 2:
            """sort by sender"""
            self.emails.sort(key=lambda email: email.sAddr, reverse=rev)
        else:
            print('ERROR')

    def create_box(self):
        """create new box to store emails"""
        pass

    def delete(self, email):
        """delete this email"""
        self.emails.remove(email)

    def open(self, email):
        """open this email"""
        email.print_email()

    def flag(self, email, flag):
        """flag email"""
        email.read()

    def move(self, email, box):
        """move this email to this box"""
        self.copy(email, box)
        self.delete(email)

    def copy(self, email, box):
        """copy this email to this box"""
        box.add_email(email)

    def save_draft(self, email, drafts):
        drafts.add_email(email)

    def display(self):
        """display email list in this inbox"""
        Box.print_list(self.emails)

    @staticmethod
    def print_list(email_list):
        """prints email list"""
        for i in xrange(len(email_list)):
            email_list[i].print_email()