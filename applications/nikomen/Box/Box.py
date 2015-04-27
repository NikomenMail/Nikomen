__author__ = 'angeloluna'

from abc import ABCMeta, abstractmethod


class Box(object):
    """abstract box object used to create all the boxes to store emails in."""
    __metaclass__ = ABCMeta

    name = "Box"  # name of the Box
    emails = [ ]  # list of emails
    location = "location"  # location???
    list = []

    def retrieve_email(self, email):
        """Retrieve email from server"""
        pass

    def filter(self):
        """Filter email on conditions"""
        pass

    def sort(self, condition):
        """sort email by conditions, 1 """
        if condition == 0:
            """sort by date"""
            list.sort(key=lambda email: email.time, reverse=True)
        elif condition == 1:
            """sort by subject"""
            list.sort(key=lambda email: email.subject, reverse=True)
        elif condition == 2:
            """sort by sender"""
            list.sort(key=lambda email: email.sAddr, reverse=True)
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
        pass

    def open(self, email):
        """open this email"""
        pass

    def write(self):
        """write a new email"""
        pass

    def flag(self, email, flag):
        """flag email"""
        pass

    def move(self, email, box):
        """move this email to this box"""
        pass

    def copy(self, email, box):
        """copy this email to this box"""
        pass



