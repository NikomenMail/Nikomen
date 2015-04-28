__author__ = 'angeloluna'

from abc import ABCMeta, abstractmethod


class Box(object):
    """abstract box object used to create all the boxes to store emails in."""
    __metaclass__ = ABCMeta

    name = "Box"  # name of the Box
    emails = [ ]  # list of emails
    location = "location"  # location???

    def retrieve_email(self, email):
        self.emails.append(email)

    def filter(self, condition, item):
        """Filter email on conditions"""
        filtered_list = []

        if condition == 0:
            """filter by subject"""
            for i in xrange(len(self.emails)):
                if self.emails[i].subject == item:
                    filtered_list.append(self.emails[i])

        elif condition == 1:
            for i in xrange(len(self.emails)):
                if self.emails[i].sAddr == item:
                    filtered_list.append(self.emails[i])
        else:
            print('ERROR')

        Box.print_list(filtered_list)

    def sort(self, condition):
        """sort email by conditions, 1 """
        if condition == 0:
            """sort by date"""
            self.emails.sort(key=lambda email: email.time, reverse=False)
        elif condition == 1:
            """sort by subject"""
            self.emails.sort(key=lambda email: email.subject, reverse=False)
        elif condition == 2:
            """sort by sender"""
            self.emails.sort(key=lambda email: email.sAddr, reverse=False)
        else:
            print('ERROR')

    def view_list(self):
        """view list of emails"""
        pass

    def create_box(self):
        """create new box to store emails"""
        pass

    def delete(self, email):
        """delete this email"""
        self.emails.remove(email)

    def open(self, email):
        """open this email"""
        pass

    @staticmethod
    def write(self):
        """write a new email"""
        pass

    def flag(self, email, flag):
        """flag email"""
        email.read()

    def move(self, email, box):
        """move this email to this box"""
        pass

    def copy(self, email, box):
        """copy this email to this box"""
        pass

    def display(self):
        """display email list in this inbox"""
        Box.print_list(self.emails)

    @staticmethod
    def print_list(email_list):
        """overloaded display method that displays any list of emails"""
        for i in xrange(len(email_list)):
            print email_list[i].time
            print "   Subject: " + email_list[i].subject