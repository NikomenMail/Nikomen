#!/usr/bin/python2.7


class AddressBook:
    """This class maintains multiple addresses for an account"""
    def __init__(self, persons, maillists):
        """The constructor of an Address Book"""
        self.personList = []
        self.mailLists = []
        #For every person add them to the list
        for p in persons:
            self.add_person(p)
        #For every mail list add it to the list
        for m in maillists:
            self.add_mail_list(m)

    def add_person(self, person):
        """Adds a new Person class to the list in the Address Book instance"""
        self.personList.append(person)

    def add_mail_list(self, maillist):
        """Adds a new MailList class to the list in the Address Book instance"""
        self.mailLists.append(maillist)

    def get_contact(searchString):
        """Implement Search Methods"""
        return None

    def get_by_mail_list(searchString):
        """Implement Search Methods"""
        return None

    def delete_contact(self, contactName):
        print "Implement delete contact!"

    def delete_mail_list(self, mailListName):
        """NEEDS better implementation, add Name parameter to MailList class"""
        self.mailLists.remove(mailListName)

    def find_email(search):
        """NEEDS call for search"""
        return None
