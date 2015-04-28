#!/usr/bin/python2.7

from applications.nikomen.modules.account_classes.contact import Contact

class MailList(Contact):
    """This is the Mail List Class. It is a subclass of
    the Contact Superclass"""
    def __init__(self, name, description=None):
        self.name = name
        self.description = description
    def setDescription(self, description):
        """Sets the description of a MailList Instance"""
        self.description = description
    def returnDescription(self):
        """Returns the description of the MailList instance"""
        return self.description
    def deleteDescription(self):
        """Deletes the description"""
        #This maybe should be handled higher up, just set the description to none
        self.description = None
