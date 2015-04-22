#!/usr/bin/python2.7

from person import Person
from maillist import MailList

class AddressBook:
    def __init__(self, persons, maillists):
        """The constructor of an Address Book"""
        self.personList = []
        self.mailLists = []
        #For every person add them to the list
        for p in persons:
            addPerson(p)
        #For every mail list add it to the list
        for m in maillists:
            addMailList(m)
    def addPerson(self, person):
        """Adds a new Person class to the list in the Address Book instance"""
        self.personList.append(person)
    def addMailList(self, maillist):
        """Adds a new MailList class to the list in the Address Book instance"""
        self.mailLists.append(maillist)
    def deleteContact(self, contactName):
        print "Implement delete contact!"
    def deleteMailList(self, mailListName)
        """NEEDS better implementation, add Name parameter to MailList class"""
        self.mailLists.remove(mailListName)
